# Web scraping refers to searching and extracting data from websites using computer programs.


# What is Data Parsing?
# Data parsing is the process of extracting useful information from a raw data source.

# what is beautiful soup
# Beautiful Soup is a Python library used for web scraping purposes to pull data out of HTML and XML files

import requests


def fetchToHtml(url,path):
 
   r= requests.get(url)
   with open(path,"w", encoding="utf-8") as f:
    f.write(r.text)


url="https://timesofindia.indiatimes.com/"

fetchToHtml(url,"dataa/times.html")