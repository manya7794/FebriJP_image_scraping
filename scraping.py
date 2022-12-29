from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


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
    driver = webdriver.Chrome(
        options=options, service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(link)
    return driver


def define_path(link: str):
    """Change the current directory to a new to download the images

    Args:
        link (str): Link of the article
    """
    # Creation of the pics folder
    try:
        os.mkdir("pics")
    except FileExistsError:
        print(
            "Directory pics already exists",
        )
    except OSError as error:
        print(error)
    os.chdir("pics")

    # Creation of the article folder
    try:
        download_folder = os.mkdir(link.split("/")[-2])
    except FileExistsError:
        print("Directory %s already exists" % (link.split("/")[-2]))
    except OSError as error:
        print(error)
    os.chdir(link.split("/")[-2])


def get_pictures(driver: webdriver, link: str):
    """Download of all pics in the article in a folder named after the article url

    Args:
        driver (webdriver): Driver used by Selenium
        link (str): Link of the article
    """
    define_path(link)

    # Picture in the banner
    try:
        picture = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/img")
        # download the image
        image_name = picture.get_attribute("src").split("/")[-1]
        print(image_name)
        urllib.request.urlretrieve(picture.get_attribute("src"), image_name)
    except Exception:
        print(
            "No element located at the banner emplacement",
        )

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
            print(image_name)
            urllib.request.urlretrieve(picture.get_attribute("src"), image_name)
        except Exception:
            print("No element located at emplacement", i)
        i += 1

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
            print(image_name)
            urllib.request.urlretrieve(picture.get_attribute("src"), image_name)
        except Exception:
            print("No element located at emplacement", i)
        i += 1
