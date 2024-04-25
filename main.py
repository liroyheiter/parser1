import requests
from bs4 import BeautifulSoup
url = 'https://ofd.soliq.uz/check?t=NA000000045091&r=797&c=20230227163754&s=320148011275'
response = requests.get(url)

bs = BeautifulSoup(response.text, "lxml")
script = bs.find("div", class_="ticket-wrap")
print(script.text)
