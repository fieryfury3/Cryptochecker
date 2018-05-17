from bs4 import BeautifulSoup
import requests
import re
# Need to show biggest cumulative growth for 1 and 24 hours, and seven days, small volumes filtered out
url = 'https://coinmarketcap.com/'
Market = requests.get(url)
soup = BeautifulSoup(Market.content, "html.parser")
(soup.prettify())
currency_table = soup.find_all("table", id="currencies")
currency_names = soup.find_all("a", class_="currency-name-container")
currency_volume = soup.find_all("a", class_="volume")
currency_price = soup.find_all("a", class_="price")
currency_24h_change = soup.find_all("td")
coin = input().lower() + "/"
print(coin)
def coinname():
    for coin_name in currency_names:
        coins = coin_name.text.lower().replace(" ", "") + '/' # Can't get coins with two words in name?
        print(coins)
        if coin == coins:
            coinvolume()

def coinvolume():

    for coin_volume in currency_volume:
        x = re.search(coin, str(coin_volume))
        if x != None:
            print(coin_volume.text)



def coinprice():
    for coin_price in currency_price:
        coin_price.text
def price_24h_change():
    for price_change_24h in currency_24h_change:
        percent = price_change_24h.get("data-percentusd")
        if percent != None:
            percent
coinname()
