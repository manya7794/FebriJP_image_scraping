import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def main(link=None, file=None):
    """_summary_

    Args:
        link (str, optional): Link to Febri Page you want to get the images. Defaults to None.
        file (str, optional): Path to the file containing links of multiple febri pages. Defaults to None.
    """
    if link is not None:
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(
            options=options, service=ChromeService(ChromeDriverManager().install())
        )
        driver.get(link)
        title = driver.title
        print(title)
        driver.quit()
        return title


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--link", "-l", type=str, help="Link to Febri Page you want to get the images"
    )
    parser.add_argument(
        "--file",
        "-f",
        type=str,
        help="Path to the file containing links of multiple febri pages",
    )

    args = parser.parse_args()
    main(args.link, args.file)
