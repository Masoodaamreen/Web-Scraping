import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)
