# Lab1

name: Batuhan Aydin

USCID: 9861477052

This lab is about web scraping. The code scrapes the CNBC World page HTML using Selenium, and then filters the HTML
with BeatifulSoup to get the data from market banner and latestNews list and turn it into CSV files.

## Setup (.venv)
Open the terminal from the lab root which is the folder that contain the "batuhan_aydin_9861477052" folder.

Then Run:
**source .venv/bin/activate**

This is to connect to the ".venv" I have created. You should run this from the root every time you open a new terminal.

## 1) Scraping the HTML
First you need your working directory to be the "scripts" folder.
To get there from the root, Run:<br>
**cd batuhan_aydin_9861477052/scripts**

Then to scrape the HTML of the CNBC website, Run:<br>
**python3 web_scraper.py**

This will create the html file "web_data.html" into the directory: batuhan_aydin_9861477052/data/raw_data/

## 2) Data Filtering
Again from the same scripts folder, Run:<br>
**python3 data_filter.py**

This will read the "web_data.html" and create two files:
- *market_data.csv* into batuhan_aydin_9861477052/data/processed_data/
- *news_data.csv* into batuhan_aydin_9861477052/data/processed_data/
