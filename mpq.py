import requests
from bs4 import BeautifulSoup
import time
from config import headers, url

while True:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    buy_button = soup.select_one(".btn-b")

    if buy_button and "displaynone" not in buy_button.get("class", []):
        print("BUY NOW!")
    else:
        print("품절입")
    time.sleep(1)