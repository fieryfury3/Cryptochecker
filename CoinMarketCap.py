import locale
import requests

locale.setlocale(locale.LC_ALL, '')

url = "https://api.coinmarketcap.com/v2/ticker/"
data = requests.get(url)
data_json = data.json()["data"]

def search():
    print(
        "Please type name or symbol to view a single coin or 'All' to view Top 100. Type 1h, 24h, 7d for price change in percentage or type volume to search coins by 24 hour volume.")
    coin = input().lower()  # input of user, forced to lowercase to match coin_name
    if coin == "volume":
        print("Type Minimum Volume in USD:")
        global volume_min
        volume_min = input()
    for id in data_json.values():
        global coin_name
        coin_name = id["name"].lower()  # name in coinmarketcap database
        global coin_symbol
        coin_symbol = id["symbol"].lower()  # symbol in database
        global hour_24_change
        hour_24_change = id["quotes"]["USD"]["percent_change_24h"]
        global hour_1_change
        hour_1_change = id["quotes"]["USD"]["percent_change_1h"]
        global day_7_change
        day_7_change = id["quotes"]["USD"]["percent_change_7d"]
        global hour_24_volume_int
        hour_24_volume_int = '{:,.0f}'.format(int(id["quotes"]["USD"]["volume_24h"]))
        global hour_24_volume_str
        hour_24_volume_str = id["quotes"]["USD"]["volume_24h"]

        if coin == "all":         #Show all(Top 100) coin information
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
                print("24h Volume: " + "$" + hour_24_volume_int)
                print("\n\n\n")

        if coin == "volume":            #Search by a minimum volume in USD
            try:
                if hour_24_volume_str >= int(volume_min):
                    print("Name: " + id["name"])
                    print("Symbol: " + id["symbol"])
                    print("Price: " + locale.currency(id["quotes"]["USD"]["price"], grouping=True))
                    print("Market Cap: " + locale.currency(id["quotes"]["USD"]["market_cap"], grouping=True))
                    print("Circulating Supply: " + '{:,.0f}'.format(int((id["circulating_supply"]))))
                    print("Total Supply: " + '{:,.0f}'.format(int((id["total_supply"]))))
                    print("1 hour change: " + str(hour_1_change) + "%")
                    print("24 hour change: " + str(hour_24_change) + "%")
                    print("7 day change: " + str(day_7_change) + "%")
                    print("24h Volume: " + "$" + hour_24_volume_int)
                    print("\n\n\n")

            except:
                print("Incorrect Input (Check to make sure you are typing an integer)\n")
                search()


        elif coin == "24h" and hour_24_change >= 5:  # Prints name and percentage if the coin has increased in value more than 5% in the past 24 hours
            print(coin_name.title())
            print("24 hour change: " + str(hour_24_change) + "%" + "\n")

        elif coin == "1h" and hour_1_change >= 5:  # Prints name and percentage if the coin has increased in value more than 5% in the past hour
            print(coin_name.title())
            print("1 hour change: " + str(hour_1_change) + "%" + "\n")

        elif day_7_change is not None and coin == "7d" and day_7_change >= 5:  # Prints name and percentage if the coin has increased in value more than 5% in the past 7 days
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
            print("24h Volume: " + "$" + hour_24_volume_int)

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
            print("24h Volume: " + "$" + hour_24_volume_int)

    else:
        search()


search()  # Calls on the function search()
