#imports
import csv
from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path("../data/raw_data/web_data.html")

print(f"Reading the html: {html_path}")
# creating a soup object using lxml
soup = BeautifulSoup(html_path.read_text(encoding="utf-8", errors="ignore"), "lxml")

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Market
print("Extracting Market banner.")
market_rows = []

# getting the market items, since we sused selenium now we can extract these with select function of beatifulsoup
for card in soup.select(".MarketCard-container"):
    # getting the market symbol.
    sym_el = card.select_one(".MarketCard-symbol")
    # getting the stock position price.
    pos_el = card.select_one(".MarketCard-stockPosition")
    # getting the changes in percentage.
    pct_el = card.select_one(".MarketCard-changesPct") or card.select_one(".MarketCard-changePct")
    if not sym_el:
        # skip if there is no market symbol.
        continue
# building one row per market item. Adding them to the list.
    market_rows.append({
        # append the market symbol
        "marketCard_symbol": sym_el.get_text(strip=True),
        # append the stock position, the amount
        "marketCard_stockPosition": pos_el.get_text(strip=True) if pos_el else "",
        # append getting the market change percentage
        "marketCard-changePct": pct_el.get_text(strip=True) if pct_el else "",
    })

print("Extraction completed. Storing Market data.")
# writing the 3 items into the CSV file.
with open("../data/processed_data/market_data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["marketCard_symbol", "marketCard_stockPosition", "marketCard-changePct"])
    w.writeheader()
    w.writerows(market_rows)
print("CSV successfully created: ..data/processed_data/market_data.csv")

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Latest News
print("Extracting LatestNews data.")
news_rows = []
# similar to the market, we use the select to get the  entries we want.
# The loop will traverse each entry and store the ones that are asked in instructions.
for item in soup.select(".LatestNews-item"):
    ts_el = item.select_one(".LatestNews-timestamp")
    a_el = item.select_one("a.LatestNews-headline")
    if not a_el:
        # did not store if the headline is missing.
        continue
    href = a_el.get("href", "")
    # getting the link href and normalize the cnbc links cause it was distorted.
    link = ("https:" + href) if href.startswith("//") else ("https://www.cnbc.com" + href) if href.startswith("/") else href

    # appending to the news_rows
    news_rows.append({
        "LatestNews-timestamp": ts_el.get_text(strip=True) if ts_el else "",
        "title": a_el.get_text(strip=True),
        "link": link,
    })

print("Extraction completed. Storing News data.")
# saving the news data as CSV.
with open("../data/processed_data/news_data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["LatestNews-timestamp", "title", "link"])
    # made sure the column names are in same order as the instructions.
    w.writeheader()
    w.writerows(news_rows)
print("CSV succcessfully created: ..data/processed_data/news_data.csv")

