import requests 
from bs4 import BeautifulSoup 
import sqlite3

url = 'https://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'text')
tags = soup.find_all('div', class_ = 'text')

for i in range(quotes):
    print(quotes[i])
    print(authors[i])

for tag in tags:
    print(tag.text.split()[1:])


conn = sqlite3.connect("web-scraping\data_from_web.db")
cursor = conn.cursor()

createTable = '''
    CREATE TABLE IF NOT EXISTS quotes (
        author TEXT
        quote_text TEXT
        tags TEXT
    )
'''

cursor.execute(createTable)

insert = '''
    INSERT INTO quotes (author, quote_text, tags)
    VALUES (?, ?, ?)
'''

for i in range(len(quotes)):
    author = authors[i].text
    quote = quotes[i].text
    tag = ", ".join(tags[i].text.split()[1:])

    cursor.execute(insert, [author, quote, tag])
    conn.commit()

        
