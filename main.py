import argparse
import scraping


def main(link=None, file=None):
    """Switch between link mode or file mode

    Args:
        link (str, optional): Link to Febri Page you want to get the images. Defaults to None.
        file (str, optional): Path to the file containing links of multiple febri pages. Defaults to None.
    """
    if link is not None:
        driver = scraping.driver_link(link)
        scraping.get_pictures(driver, link)
        driver.quit()


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
