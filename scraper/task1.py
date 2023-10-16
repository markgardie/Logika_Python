import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')

authors_dict = dict()

for i in range(len(authors)):
    authors_dict[authors[i].text] = quotes[i].text

with open("scraper\result.json", "w", encoding="utf-8") as file:
    json.dump(authors_dict, file)