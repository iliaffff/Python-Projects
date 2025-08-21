import requests
import bs4
from pathlib import Path
import time
from khayyam import JalaliDatetime

currentDate = JalaliDatetime.now().date()

varzesh3_url = "https://www.varzesh3.com/news"
tasnim_url = "https://www.tasnimnews.com/"
mehr_url = "https://www.mehrnews.com/"

# Varzesh 3
def varzesh3():
    Path("Web Scraping For News Websites/varzesh3").mkdir(exist_ok=True)
    Path(f"Web Scraping For News Websites/varzesh3/{currentDate}").mkdir(exist_ok=True)
    response = requests.get(varzesh3_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    htmlText = open("file.txt", "a", encoding="utf-8")
    htmlText.write(soup.prettify())
    titleName = soup.find_all("span", attrs={"class": "v31h7i4cw v31ua5tub v3104kibb v3fifm61 v317e3ifc v3a7kkou v3117nqv4 v3at24cr v3b3r6kr v3lyipyv v3wc7x28"})
    textFile = open(f"Web Scraping For News Websites/varzesh3/{str(currentDate)}/{titleName[0].text}", "a", encoding="utf-8")

    for i in soup.find_all("a", href=True):
        href = i['href']
        if href.startswith("http") and titleName[0].text.split()[0] in href:
            var1 = requests.get(href)
            soup1 = bs4.BeautifulSoup(var1.text, "html.parser")
            newsText = soup1.find_all("p", attrs={"style": "text-align:justify"})
            for item in newsText:
                textFile.write(f"{item.text}\n\n")
            break
    textFile.close()
    
    

    
    # linkList = soup.find("a", attrs={"href"})
    # linkList = open(f"") 
    # for i in range(len(titleName)):
    #     textFile = open(f"Web Scraping For News Websites/varzesh3/{currentDate}/{titleName[i].text}", "a", encoding="utf-8")
    # newsText = soup.find_all("p", attrs={"style": "text-align:justify"})
    # for news in newsText:
    #     textFile.write(f"{news.text}\n\n")
    # textFile.close()
    
# def tasnim():
#     Path("Web Scraping For News Websites/tasnim").mkdir(exist_ok=True)
#     response = requests.get(tasnim_url)
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     newsList = soup.find_all("h4", attrs={"class": "lead"})
#     Path(f"Web Scraping For News Websites/varzesh3/{currentDate}").mkdir(exist_ok=True)    
#     for news in newsList:
#         textFile.write(f"{news.text}\n\n")
#     textFile.close()

# def mehrNews():
#     Path("Web Scraping For News Websites/mehrnews").mkdir(exist_ok=True)
#     response = requests.get(mehr_url)
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     newsList = soup.find_all("p")
#     Path(f"Web Scraping For News Websites/varzesh3/{currentDate}").mkdir(exist_ok=True)    
#     for news in newsList:
#         if "All" not in news.text:
#             textFile.write(f"{news.text}\n\n")
#     textFile.close()


varzesh3()
# tasnim()
# mehrNews()



