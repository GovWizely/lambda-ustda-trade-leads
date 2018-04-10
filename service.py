# -*- coding: utf-8 -*-
import datetime as dt
import json
import xml.etree.ElementTree as ET

import boto3
import requests

XML_ENDPOINT = 'https://www.ustda.gov/api/tradeleads/xml'
RSS_ENDPOINT = 'https://www.ustda.gov/business-opportunities/trade-leads/feed'

s3 = boto3.resource('s3')


def handler(event, context):
    entries = get_entries()
    if len(entries) > 0:
        s3.Object('trade-leads', 'ustda.json').put(Body=json.dumps(entries),
                                                   ContentType='application/json')
        return "Uploaded ustda.json file with %i trade leads" % len(entries)
    else:
        return "No entries loaded from %s so there is no JSON file to upload" % RSS_ENDPOINT


def get_entries():
    title_link_dict = get_items()
    print("Fetching XML feed of items...")
    response = requests.get(XML_ENDPOINT)
    root = ET.fromstring(response.text.encode('utf-8'))
    nodes = root.findall('node')
    entries = [get_entry(node, title_link_dict) for node in nodes]
    print("Found %i entries" % len(entries))
    return entries


def get_entry(node, title_link_dict):
    entry = {kid.tag.lower().replace('-', '_'): kid.text.strip() for kid in node.getchildren() if
             kid.text and len(kid.text) > 0}
    entry['title'] = entry['title'].strip()
    entry['url'] = title_link_dict.get(entry['title'], None)
    entry['open_date'] = normalize_date(entry['open_date'])
    entry['close_date'] = normalize_date(entry['close_date'])
    return entry


def normalize_date(entry_date):
    return dt.datetime.strptime(entry_date, '%m/%d/%Y').strftime("%Y-%m-%d")


def get_items():
    print("Fetching RSS feed of items...")
    response = requests.get(RSS_ENDPOINT)
    root = ET.fromstring(response.text.encode('utf-8'))
    items = root.findall('./channel/item')
    title_link_dict = {item.find('title').text.strip(): item.find('link').text for item in items}
    print("Found %i items" % len(title_link_dict))
    return title_link_dict
