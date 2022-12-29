import main as script
from selenium import webdriver


def test_main():
    assert script.main(link="https://www.google.fr/").title == "Google"
