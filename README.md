# Downloading images of articles on the Febri.jp website

The purpose of this script is to allow you to download the photos available on the articles of Febri.jp automatically. 

**Disclaimer:** The use of this script is only for personal use

## 1. Installation 

Download the project to your directory via a terminal by entering the following command:
```
git clone https://github.com/easterbuunny/Jeu_Python.git
```
Make sure you have Python 3.9 or higher installed on your computer and then run the following command in a terminal opened in the folder containing the project:
```
pip install -r .\requirements.txt
```

## 2. How to use the script

Open a terminal in the project folder and run the following command: 

```
python .\main.py -l ARTICLE_URL
# or
python .\main.py -f ARTICLES_FILE
```

Once the script has finished running, you will be able to find the images in the *pics* folder containing all the subfolders whose names are based on the URLs of the articles.