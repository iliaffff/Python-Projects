News Scraper

Overview

This Python project automatically collects daily news from selected news websites at specified times. The script connects to multiple news websites, fetches the latest news, and organizes them in a structured folder system.

Features

Connects to multiple news websites.
Collects news published on the current day.
Creates a separate folder for each news website.
Stores all news texts in a single file inside the corresponding folder.

How it Works

The script connects to each website using requests and parses the page with BeautifulSoup.
It extracts the news text according to the site's HTML structure.
It creates a folder for each news website if it doesn't exist.
It saves all news for the day in a text file named after the current date.

Requirements

Python 3.x

Libraries:
requests
beautifulsoup4