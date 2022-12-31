import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import urllib.request
from selenium.webdriver.common.by import By
import os


def driver_init():
    """Driver initialization for threading

    Returns:
        webdriver: New Selenium driver
    """
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path="chomedriver.exe")
    return driver


def driver_link(link: str):
    """Open the driver on the specified link and return it

    Args:
        link (str): Link to open in the webdriver element

    Returns:
        webdriver: Driver created by Selenium
    """
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path="chomedriver.exe")
    driver.get(link)
    return driver


def check_pics_folder():
    """Checking of pics folder existence, create it if inexistant"""
    # Creation of the pics folder
    try:
        os.mkdir("pics")
    except FileExistsError:
        pass
    except OSError as error:
        print(error)

    try:
        os.chdir("pics")
    except Exception:
        pass


def define_path(link: str):
    """Define the download path for the pictures in the article

    Args:
        link (str): Link of the article

    Returns:
        str: Path to download folder
    """
    # Creation of the article folder
    download_folder = link.split("/")[-2]
    try:
        os.mkdir(download_folder)
    except FileExistsError:
        print("Directory %s already exists" % (link.split("/")[-2]))
    except OSError as error:
        print(error)

    return download_folder + "/"


def get_pictures_from_figure(driver, downloading_path):
    """Download the pictures contained in figure element

    Args:
        driver (webdriver): Driver created by Selenium
        downloading_path (str): Path to download folder
    """
    # Pictures in figure elements
    i = 0
    while i < 30:
        try:
            picture = driver.find_element(
                By.XPATH,
                "/html/body/div[1]/div[4]/div/div[1]/div[1]/div[3]/div[1]/div["
                + str(i)
                + "]/figure/img",
            )
            # download the image
            image_name = picture.get_attribute("src").split("/")[-1]
            print(
                f"Downloading {image_name} at {downloading_path}",
            )
            urllib.request.urlretrieve(
                picture.get_attribute("src"), downloading_path + image_name
            )
        except Exception:
            pass
        i += 1


def get_pictures_from_img(driver, downloading_path):
    """Download the pictures contained in img element

    Args:
        driver (webdriver): Driver created by Selenium
        downloading_path (str): Path to download folder
    """
    # Picture in img elements
    i = 0
    while i < 30:
        try:
            picture = driver.find_element(
                By.XPATH,
                "//*[@id='blocks_general_field']/div[" + str(i) + "]/img",
            )
            # download the image
            image_name = picture.get_attribute("src").split("/")[-1]
            print(
                f"Downloading {image_name} at {downloading_path}",
            )
            urllib.request.urlretrieve(
                picture.get_attribute("src"), downloading_path + image_name
            )
        except Exception:
            pass
        i += 1


def get_pictures(driver: webdriver, link: str):
    """Download of all pics in the article in a folder named after the article url

    Args:
        driver (webdriver): Driver used by Selenium
        link (str): Link of the article
    """
    try:
        downloading_path = define_path(link)
        # Check driver URL
        if driver.current_url != link:
            driver.get(link)
        # Picture in the banner
        try:
            picture = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/img")
            # download the image
            image_name = picture.get_attribute("src").split("/")[-1]
            print(f"Downloading {image_name} at {downloading_path}")
            urllib.request.urlretrieve(
                picture.get_attribute("src"),
                downloading_path + image_name,
            )
        except Exception:
            print(
                f"No element located at the banner emplacement for {link}",
            )

        # Thread for pictures in figure elements
        t1 = threading.Thread(
            target=get_pictures_from_figure, args=(driver, downloading_path)
        )
        # Thread for pictures in img elements
        t2 = threading.Thread(
            target=get_pictures_from_img, args=(driver, downloading_path)
        )

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    except Exception as e:
        print(e)
