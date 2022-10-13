# web-scraping
**HHA507 / Data Science / Assignment 7 / Webscraping**


## This repo aims to:
1. Write a .py script to webscrap, focusing on the __*beautifulsoup4*__ package
2. Create a dataframe with structured data for each website and export to a new .csv


## Websites Used:
**1. https://hitconsultant.net/category/health-it/**
- a health information technology news source

**2. https://realpython.github.io/fake-jobs/**
- a dummy job board created for the purpose of practicing webscrapping 

## Required Python Packages: 
1. beautifulsoup4
2. pandas
3. requests 

## div/classes/css tags I used to extract information:
**1. hit_news.py**
- titles = soup.find_all('a',class_='entry-title-link')
- class_='entry-title-link')
- authors = soup.find_all('span', class_='entry-author-name')
- dates = soup.find_all('time', class_='entry-time')
- descriptions = soup.find_all('div', class_='entry-content')

**2. job_board.py**
- job_titles = soup.find_all('h2',class_='title is-5')
- company_names = soup.find_all('h3', class_='subtitle is-6 company')
- dates = soup.find_all('p', class_='is-small has-text-grey')
- locations = soup.find_all('p', class_='location')