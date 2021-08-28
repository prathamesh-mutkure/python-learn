import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.in/Digitek-DTR-550-LW-Tripod/dp/B074CWD7MS/ref=sr_1_1_sspa?dchild=1&keywords=tripod" \
              "&qid=1630050176&sr=8-1-spons&psc=1&spLa" \
              "=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQzZUTkJKR1ZBWkVLJmVuY3J5cHRlZElkPUEwMDkzNDMxOVRNN09EQlJYWVoyJmVuY3J5cHRlZEFkSWQ9QTAyODE1MzcxMTE4TU5DTDhaSUxDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== "

BUY_PRICE = 1400.0

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.131 Safari/537.36",
}

response = requests.get(PRODUCT_URL, headers=headers)
response.raise_for_status()

web_content = response.text
soup = BeautifulSoup(web_content, "html.parser")

price_tag = soup.find(name="span", id="priceblock_ourprice")
price_string = price_tag.get_text().split(".")[0]
price_string = ''.join(filter(str.isnumeric, price_string))
current_price = float(price_string)

if current_price <= BUY_PRICE:
    print("Go, buy it fast")
else:
    print("Wait, till price comes down")
