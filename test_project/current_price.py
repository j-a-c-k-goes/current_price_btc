# --- imoprt modules ---
import requests
import math

# --- get time until next block mined ---
def btc_eta ():
    btc_eta = requests.get("https://blockchain.info/q/eta")
    output = print(f"time until next block mined\t{btc_eta.text} seconds".upper())
    return output

# --- get bicoin circulation ---
def btc_circulation():
    btc_circulation = requests.get("https://blockchain.info/q/totalbc")
    output = print(f"current circulation\t{btc_circulation.text} btc".upper())
    return output

# --- get price of bitcoin ---
def btc_price():
    btc_price = requests.get("https://blockchain.info/q/24hrprice")
    output = print(f"current price of bitcoin\t${btc_price.text}".upper())
    return output

if __name__ == "__main__":
    btc_eta()
    btc_circulation()
    btc_price()
