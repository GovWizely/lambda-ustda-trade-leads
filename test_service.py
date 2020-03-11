import vcr

from service import get_entries


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
