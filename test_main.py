import main as script

import scraping


def test_driver():
    assert scraping.driver_link("https://www.google.fr/") is not None
