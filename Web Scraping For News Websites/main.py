import requests
import bs4
from pathlib import Path
import time

currentDate = time.strftime("%Y-%m-%d", time.localtime())

varzesh3_url = "https://www.varzesh3.com/news"
tasnim_url = "https://www.tasnimnews.com/"
mehr_url = "https://www.mehrnews.com/"

#Varzesh 3
def varzesh3():
    Path("Web Scraping For News Websites/varzesh3").mkdir(exist_ok=True)
    response = requests.get(varzesh3_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    newsList = soup.find_all("p", attrs={"class": "v3if65rj v31gp4ges v31hr2gdg v31xmf6yo v31s85apg v3devi71"})
    textFile = open(f"Web Scraping For News Websites/varzesh3/{currentDate}.txt", "a", encoding="utf-8")
    for news in newsList:
        textFile.write(f"{news.text}\n\n")
    textFile.close()
    
def tasnim():
    Path("Web Scraping For News Websites/tasnim").mkdir(exist_ok=True)
    response = requests.get(tasnim_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    newsList = soup.find_all("h4", attrs={"class": "lead"})
    textFile = open(f"Web Scraping For News Websites/tasnim/{currentDate}.txt", "a", encoding="utf-8")
    for news in newsList:
        textFile.write(f"{news.text}\n\n")
    textFile.close()

def mehrNews():
    Path("Web Scraping For News Websites/mehrnews").mkdir(exist_ok=True)
    response = requests.get(mehr_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    newsList = soup.find_all("p")
    textFile = open(f"Web Scraping For News Websites/mehrnews/{currentDate}.txt", "a", encoding="utf-8")
    for news in newsList:
        if "All" not in news.text:
            textFile.write(f"{news.text}\n\n")
    textFile.close()


varzesh3()
tasnim()
mehrNews()

