# Lab1

name: Batuhan Aydin

USCID: 9861477052

This lab is about web scraping. The code scrapes the CNBC World page HTML using Selenium, and then filters the HTML
with BeatifulSoup to get the data from market banner and latestNews list and turn it into CSV files.

## Setup (Ubuntu)

**Note:** The instructions below are written for Ubuntu (Virtual Machine). If running on Windows, the Firefox/geckodriver install paths may differ and needs to be fixed!

Open the terminal from the lab root which is the folder that contain the "batuhan_aydin_9861477052" folder.

Then Create a virtual environment:<br>
**python3 -m venv .venv**<br>
**source .venv/bin/activate**

This is to connect to the ".venv". You should run this from the root every time you open a new terminal if set it up once.

Then to install the Python dependencies, Run:<br>
**pip install selenium beautifulsoup4 lxml**

Also from the ubuntu terminal, Run:<br>
**sudo apt update**<br>
**sudo apt install -y firefox**<br>
**sudo apt install -y firefox-geckodriver**

Verify geckodriver path (this project expects /usr/bin/geckodriver):<br>
**which geckodriver**

If it is not "/usr/bin/geckodriver", force it:<br>
**sudo ln -sf "$(which geckodriver)" /usr/bin/geckodriver**
**which geckodriver**

-------------------------------------------------------------------

## Setup (MacOS)

Install Firefox + geckodriver:<br>
**brew install --cask firefox**<br>
**brew install geckodriver**

find the geckodriver path:<br>
**which geckodriver**

update "web_scraper.py" to use your path:<br>
Replace:<br>
**service = FirefoxService(executable_path="/snap/bin/geckodriver")**<br>

With (use the output from **which geckodriver**, for example "/opt/homebrew/bin/geckodriver"):<br>
**service = (executable_path="YOUR_GECKODRIVER_PATH_HERE")**

------------------------------------------------------------------

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
