from bs4 import BeautifulSoup
import requests
import os

# Notes: Market banner:
#It is  a section with class:"MarketsBanner-container"

# Section Titled "Latest News":
# It is a div with class="LatestNews-isHomePage LatestNews-isIntlHomepage"

url = "https://www.cnbc.com/world/?region=world"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# request the access to the website using headers (without headers, the response is blocked)
html = requests.get(url, headers=headers).text
# Parse the html using bs4
soup = BeautifulSoup(html, "html.parser")
##print(soup)

# saving the file
path = "../data/raw_data/web_data.html"
with open(path, "w") as f:
  f.write(html)

