import requests


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get("https://www.zillow.com/homes/for_sale/Argyle,-TX_rb/", headers=header)

print(response)  # Prints out HTTP Status Code [200]: Good to go!