import locale
import requests
locale.setlocale(locale.LC_ALL, '')


url = "https://api.coinmarketcap.com/v2/ticker/"
data = requests.get(url)
data_json = data.json()["data"]


def searchanother():
    print("Search for another coin? (Y/N)")
    answer = input().lower()  # userinput
    if answer == "Y".lower():  # if user input is "Y"
        search()
    elif answer == "N".lower():  # if user input is "N"
        exit()
    else:  # if user input is not "Y" or "N"
        print("Not a valid answer\n")
        searchanother()


def search():
    print("Please type name or symbol to view a single coin or 'All' to view Top 100. Type 1h, 24h, 7d for price increases above 5% for relative time.")
    coin = input().lower()  # input of user, forced to lowercase to match coin_name
    for id in data_json.values():
        coin_name = id["name"].lower()  # name in coinmarketcap database
        coin_symbol = id["symbol"].lower() # symbol in database
        hour_24_change = id["quotes"]["USD"]["percent_change_24h"]
        hour_1_change = id["quotes"]["USD"]["percent_change_1h"]
        day_7_change = id["quotes"]["USD"]["percent_change_7d"]

        if coin == "all":
            for i in range(1):
                print("Name: " + id["name"])
                print("Symbol: " + id["symbol"])
                print("Price: " + locale.currency(id["quotes"]["USD"]["price"], grouping=True))
                print("Market Cap: " + locale.currency(id["quotes"]["USD"]["market_cap"], grouping=True))
                print("Circulating Supply: " + '{:,.0f}'.format(int((id["circulating_supply"]))))
                print("Total Supply: " + '{:,.0f}'.format(int((id["total_supply"]))))
                print("1 hour change: " + str(hour_1_change) + "%")
                print("24 hour change: " + str(hour_24_change) + "%")
                print("7 day change: " + str(day_7_change) + "%")
                print("24h Volume: " + "$" + '{:,.0f}'.format(int(id["quotes"]["USD"]["volume_24h"])))
                print("\n\n\n")



        elif coin == "24h" and hour_24_change >= 5:   # prints name and percentage if the coin has increased in value more than 5% in the past 24 hours
            print(coin_name.title())
            print("24 hour change: " + str(hour_24_change) + "%" + "\n")

        elif coin == "1h" and hour_1_change >= 5:   # prints name and percentage if the coin has increased in value more than 5% in the past hour
            print(coin_name.title())
            print("1 hour change: " + str(hour_1_change) + "%" + "\n")


        elif day_7_change != None and coin == "7d" and day_7_change >= 5:   # prints name and percentage if the coin has increased in value more than 5% in the past 7 days
                print(coin_name.title())
                print("7 day change: " + str(day_7_change) + "%" + "\n")



        elif coin_name == coin:
            print("Name: " + id["name"])
            print("Symbol: " + id["symbol"])
            print("Price: " + locale.currency(id["quotes"]["USD"]["price"], grouping=True))
            print("Market Cap: " + locale.currency(id["quotes"]["USD"]["market_cap"], grouping=True))
            print("Circulating Supply: " + '{:,.0f}'.format(int((id["circulating_supply"]))))
            print("Total Supply: " + '{:,.0f}'.format(int((id["total_supply"]))))
            print("1 hour change: " + str(hour_1_change) + "%")
            print("24 hour change: " + str(hour_24_change) + "%")
            print("7 day change: " + str(day_7_change) + "%")
            print("24h Volume: " + "$" + '{:,.0f}'.format(int(id["quotes"]["USD"]["volume_24h"])))
            searchanother()

        elif coin_symbol == coin:
            print("Name: " + id["name"])
            print("Symbol: " + id["symbol"])
            print("Price: " + locale.currency(id["quotes"]["USD"]["price"], grouping=True))
            print("Market Cap: " + locale.currency(id["quotes"]["USD"]["market_cap"], grouping=True))
            print("Circulating Supply: " + '{:,.0f}'.format(int((id["circulating_supply"]))))
            print("Total Supply: " + '{:,.0f}'.format(int((id["total_supply"]))))
            print("1 hour change: " + str(hour_1_change) + "%")
            print("24 hour change: " + str(hour_24_change) + "%")
            print("7 day change: " + str(day_7_change) + "%")
            print("24h Volume: " + "$" + '{:,.0f}'.format(int(id["quotes"]["USD"]["volume_24h"])))
            searchanother()

    else:
        search()


search()  # Calls on the function search()
