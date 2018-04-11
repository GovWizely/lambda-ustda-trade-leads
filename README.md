# USTDA Trade Leads Lambda

This project provides an AWS Lambda that creates a single JSON document from the RSS feed 
at [https://www.ustda.gov/business-opportunities/trade-leads/feed](https://www.ustda.gov/business-opportunities/trade-leads/feed) and the XML feed at
[https://www.ustda.gov/api/tradeleads/xml](https://www.ustda.gov/api/tradeleads/xml).
It uploads that JSON file to a S3 bucket.

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python 2.7
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

## Getting Started

	git clone git@github.com:GovWizely/lambda-ustda-trade-leads.git
	cd lambda-ustda-trade-leads
	mkvirtualenv -r requirements.txt -p /usr/bin/python2.7 lambda-ustda-trade-leads

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control

## Invocation

	lambda invoke -v
 
## Deploy

	lambda deploy --use-requirements
