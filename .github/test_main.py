import main as script


def test_main():
    assert script.main(link="https://www.google.fr/") == "Google"
