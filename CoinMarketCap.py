import requests
url = "https://api.coinmarketcap.com/v2/ticker/"
data = requests.get(url)
data_json = data.json()["data"]

def searchanother():
    print("Search for another coin? (Y/N)")
    answer = input().lower()        #userinput
    if answer == "Y".lower():       #if user input is "Y"
        search()
    elif answer == "N".lower():     #if user input is "N"
        exit()
    else:                           #if user input is not "Y" or "N"
        print("Not a valid answer\n")
        searchanother()


def search():
    print("Please type name of coin: ")
    coin = input().lower() #input of user, forced to lowercase to match coin_name
    for id in data_json.values():
        coin_name = id["name"].lower() #name in coinmarketcap database
        if coin_name == coin:
            print("Symbol: " + id["symbol"])
            print("Price: $" + str(id["quotes"]["USD"]["price"]))
            searchanother()
            break
    else:
        print("Check Spelling\n")
        search()



search() #Calls on the function search()