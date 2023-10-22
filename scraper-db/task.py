import requests
from bs4 import BeautifulSoup
import json
import sqlite3

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lmxl')
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')
tags = soup.find_all('a', class_ = 'tag')

conn = sqlite3.connect("scraper-db\scraper-db.db")
cursor = conn.cursor()

createTableSQL = "CREATE TABLE IF NOT EXIST quotes (author TEXT, quote TEXT, tag TEXT)"
cursor.execute(createTableSQL)

insertSQL = "INSERT INTO quotes (author, quote, tag) VALUES (?, ?, ?)"
for i in range(len(quotes)):
    author = authors[i]
    quote = quotes[i]
    tag = tags[i].text.split()[1:]
    cursor.execute(insertSQL, [author, quote, tag])
    conn.commit()