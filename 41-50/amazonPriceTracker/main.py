from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
SMTP_ADDRESS = os.getenv('SMTP_ADDRESS')

#url = "https://appbrewery.github.io/instant_pot/"
urls = {'Casley Phone Case':{'url':"https://www.amazon.com/Casely-Opposites-Attract-Colorblock-Mountain/dp/B09T61GD8D?ref_=ast_sto_dp",'buy-price':20}}

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}
for u in urls:
    url = urls[u]['url']
    
    res = requests.get(url,headers=header)

    soup = BeautifulSoup(res.content, "html.parser")

    price = soup.find(class_='a-offscreen').get_text()

    price = float(price.replace('$',""))

    print(price)

    title = soup.find(id='productTitle').get_text().replace(' ','')
    print(title)

    BUY_PRICE = urls[u]['buy-price']

    if price < BUY_PRICE:
        message = f"{u} is on sale for {price}!"

        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            result = connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )