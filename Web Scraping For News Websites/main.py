import requests
import bs4
from pathlib import Path
import time
import jdatetime

currentDate = jdatetime.date.today()

varzesh3_url = "https://www.varzesh3.com/news"


# Varzesh 3
def varzesh3():
    #Making Folders
    Path("Web Scraping For News Websites/varzesh3").mkdir(exist_ok=True)
    Path(f"Web Scraping For News Websites/varzesh3/{str(currentDate)}").mkdir(exist_ok=True)
    response = requests.get(varzesh3_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    htmlText = open("file.txt", "a", encoding="utf-8")
    htmlText.write(soup.prettify()) # makes a human_readable form of the html text with indentation
    #Finding all the titles of the news
    titleName = soup.find_all("span", attrs={"class": "v31h7i4cw v31ua5tub v3104kibb v3fifm61 v317e3ifc v3a7kkou v3117nqv4 v3at24cr v3b3r6kr v3lyipyv v3wc7x28"})
    for j in range(len(titleName)):
        fileName = titleName[j].text.replace(" ", "_")
        fileName = titleName[j].text.replace(":", "_")    
    textFile = open(f"Web Scraping For News Websites/varzesh3/{str(currentDate)}/{fileName}.txt", "a", encoding="utf-8")
    
    #Finding the first http link
    iterator = 0
    while iterator < len(titleName):
        for i in soup.find_all("a", href=True):
            href = i['href']
            if href.startswith("http") and titleName[iterator].text.split()[0] in href:
                #Saving the text of the first news
                var1 = requests.get(href)
                soup1 = bs4.BeautifulSoup(var1.text, "html.parser")
                newsText = soup1.find_all("p", attrs={"style": "text-align:justify"})
                for item in newsText:
                    textFile.write(f"{item.text}\n\n")
            iterator += 1
    textFile.close()
    
varzesh3()




