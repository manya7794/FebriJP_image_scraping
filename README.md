# Downloading images of articles on the Febri.jp website
[![Python application](https://github.com/manya7794/FebriJP_image_scraping/actions/workflows/python-app.yml/badge.svg)](https://github.com/manya7794/FebriJP_image_scraping/actions/workflows/python-app.yml)

The purpose of this script is to allow you to download the photos available on the articles of Febri.jp automatically. 

**Disclaimer:** The use of this script is only for personal use

## 1. Installation 

Download the project to your directory via a terminal by entering the following command:
```
git clone https://github.com/manya7794/FebriJP_image_scraping.git
```
Make sure you have Python 3.9 or higher installed on your computer and then run the following command in a terminal opened in the folder containing the project:
```
pip install -r .\requirements.txt
```


You will need to download chromedriver and drop the file in the project folder. You can download it at this adress :

https://chromedriver.chromium.org/downloads

Regarding the version to download, please go to the settings of your Google Chrome browser and check the version of the latter.

## 2. How to use the script

Open a terminal in the project folder and run the following command by replacing ARTICLE_URL or ARTICLES_FILE by the url of the article or the path of the file as appropriate: 

```
python .\main.py -l "ARTICLE_URL"
# or
python .\main.py -f "ARTICLES_FILE"
```

Once the script has finished running, you will be able to find the images in the *pics* folder of the project containing all the subfolders whose names are based on the URLs of the articles.
