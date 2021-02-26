import requests
from bs4 import BeautifulSoup


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get("https://www.zillow.com/homes/Argyle,-TX_rb/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_links_elements = soup.select(".list-card-top a")
all_links = []
for link in all_links_elements:
    href = link["href"]
    print(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ") for address in all_address_elements]
print(all_addresses)

all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text().split(" + ") for price in all_price_elements if "$" in price.text]
print(all_prices)

all_detail_elements = soup.select(".list-card-details")
all_details = [detail.get_text().split(" + ") for detail in all_detail_elements]
print(all_details)