# Import Libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get news page
page = requests.get('https://hitconsultant.net/category/health-it/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


# Get titles of each article
titles = soup.find_all('a',class_='entry-title-link')
output_titles = []
for i in titles: #for x in y: 
    print(i.text)
    data = i.text
    output_titles.append(data)

# Verify number of titles using len
len(output_titles) #10
output_titles[1] # Print title number x
output_titles[3]

# Get authors from each article
authors = soup.find_all('span', class_='entry-author-name')
output_authors = []
for i in authors:
    print('Count: ', i.text)
    data = i.text
    output_authors.append(data)

len(output_authors)
output_authors[2]

# Get dates of each article
dates = soup.find_all('time', class_='entry-time')
output_dates = []
for i in dates:
    print('Count: ', i.text)
    data = i.text
    output_dates.append(data)

len(output_dates)
output_dates[4]



# Get descriptions of each articlefind each article where class='Box-row'
descriptions = soup.find_all('div', class_='entry-content')
output_descriptions = []
for i in descriptions:
    print('Count: ', i.text)
    data = i.text
    output_descriptions.append(data)

len(output_descriptions)
output_descriptions [8]


# Compile data into a new dataframe
df = pd.DataFrame({'titles':output_titles,'authors':output_authors, 'dates':output_dates})
# Export to new csv 
df.to_csv('data/hit_news.csv')