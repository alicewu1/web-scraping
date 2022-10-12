from lib2to3.pygram import Symbols
import symbol
import pandas as pd
import requests
from bs4 import BeautifulSoup

# get top ETFs page
page = requests.get('https://finance.yahoo.com/etfs')
page
page.text


# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())



# Get list of ETF names on page 1
names = soup.find_all('td', class_="Va(m) Ta(start) Px(10px) Fz(s)")
output_names = []
for i in names:
    print(i.text)
    data = i.text
    output_names.append(data)

# Verify using len
len(output_names) #25

# Get ticker symbol of each ETF
symbols= soup.find_all('a', class_="Fw(600) C($linkColor)")
output_symbols = []
for i in symbols:
    print(i.text)
    output_symbols.append(i.text)

len(output_symbols)


# Get Prices Intraday
prices= soup.find_all('td', class_="Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)")

output_prices = []
for i in prices:
    print(i.text)
    output_prices.append(i.text)

len(output_prices)

df = pd.DataFrame({'names': output_names, 'symbols': output_symbols, 'prices': output_prices})
df