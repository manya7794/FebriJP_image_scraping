import argparse
import scraping
from concurrent.futures import ThreadPoolExecutor


def main(link=None, file=None):
    """Switch between link mode or file mode

    Args:
        link (str, optional): Link to Febri Page you want to get the images. Defaults to None.
        file (str, optional): Path to the file containing links of multiple febri pages. Defaults to None.
    """
    # Link case
    if link is not None:
        scraping.check_pics_folder()
        print("Scraping is starting for", link)
        driver = scraping.driver_link(link)
        scraping.get_pictures(driver, link)
        driver.quit()

    # File case
    if file is not None:
        print("Scraping is starting for", file)
        file = open(file, "r")
        links = file.read()
        links_list = links.split("\n")
        file.close()
        scraping.check_pics_folder()
        workers_nb = len(links_list)
        print("Creation of drivers")
        drivers = [scraping.driver_init() for _ in range(workers_nb)]
        print("Drivers created")

        with ThreadPoolExecutor(max_workers=workers_nb) as executor:
            executor.map(scraping.get_pictures, drivers, links_list)
        [driver.quit() for driver in drivers]

    # End of script
    print("Scraping has finished!!!")


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
