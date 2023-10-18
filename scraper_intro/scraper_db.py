import requests
from bs4 import BeautifulSoup
import json
import sqlite3

url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lmxl')
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')
tags = soup.find_all('div', class_='tags')

conn = sqlite3.connect("scraper_intro\scraper_db.db")
cursor = conn.cursor()

createSQL = '''CREATE TABLE IF NOT EXISTS quotes(author TEXT, quote TEXT, tags TEXT)'''
cursor.execute(createSQL)

insertSQL = '''INSERT INTO quotes (author, quote, tags) VALUES (?, ?, ?)'''
for i in range(len(quotes)):
  author = authors[i].text
  quote = quotes[i].text
  tag = ', '.join(tags[i].text.split()[1:])
  cursor.execute(insertSQL, [author, quote, tag])
  conn.commit()
