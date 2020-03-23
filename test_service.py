import xml

import vcr

from service import get_entries, handler, normalize_date


@vcr.use_cassette()
def test_get_entries():
    """Reads from the `test_get_entries` cassette and processes the entries.

    """
    entries = get_entries()
    assert len(entries) == 1
    expected_entry = {
        "title": "High Definition Data Transfer from Mobile Aerial Vehicles",
        "open_date": "2020-02-03",
        "close_date": "2020-02-07",
        "description": "Background: \n\nThe City of Cape Town, South Africa is committed",
        "url": "https://ustda.gov/business-opportunities/trade-leads/high-definition-data",
    }
    assert entries[0] == expected_entry


def test_handler_handles_parse_error(mocker):
    """Ensures any XML parsing issues from garbage input get ignored"""
    mocker.patch('service.get_entries', side_effect=xml.etree.ElementTree.ParseError)
    assert handler(None, None) is False


def test_normalize_date_handles_missing_field():
    """Ensures any missing date fields get represented as None"""
    assert normalize_date({'open_date': '10/10/2020'}, 'close_date') is None
