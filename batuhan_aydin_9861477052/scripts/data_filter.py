from bs4 import BeautifulSoup
import requests
import os

# Notes: Market banner:
#It is  a section with class:"MarketsBanner-container"

# Section Titled "Latest News":
# It is a div with class="LatestNews-isHomePage LatestNews-isIntlHomepage"

# read the html file we stored
path = "../data/raw_data/web_data.html"
with open(path,"r") as f:
  html = f.readlines()

print(len(html))
#print(html[1])



# Market Banner




# Latest News
