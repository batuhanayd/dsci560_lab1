# imports
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService

URL = "https://www.cnbc.com/world/?region=world"
out_path = "../data/raw_data/web_data.html"

# setting the options for the webdriver
options = webdriver.FirefoxOptions()
options.add_argument("-headless")

# Im using explicitly geckodriver because default firefox did not work
service = FirefoxService(executable_path="/snap/bin/geckodriver")

# setting up the driver and reding the url
driver = webdriver.Firefox(service=service, options=options)
driver.get(URL)
wait = WebDriverWait(driver, 60)

# Waiting to make sure the market banner data is retrieved.
# cnbc probably uses an API to get that data so that is probably why it requires us to wait for it to be uploaded.
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MarketCard-symbol")))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MarketCard-stockPosition")))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".MarketCard-changesPct")))

time.sleep(1)

# writing/saving the html file
with open(out_path, "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print(f"Saved the html file to: {out_path}")
driver.quit()
