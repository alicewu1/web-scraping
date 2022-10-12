# Import Libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get news page
page = requests.get('https://realpython.github.io/fake-jobs/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


# Get job titles of each posting
job_titles = soup.find_all('h2',class_='title is-5')
output_job_titles = []
for i in job_titles: #for x in y: 
    print(i.text)
    data = i.text
    output_job_titles.append(data)

# Verify number of job titles using len
len(output_job_titles) # 100
output_job_titles[1] # Print title number x
output_job_titles[3]

# Get company names of each job posting
company_names = soup.find_all('h3', class_='subtitle is-6 company')
output_company_names = []
for i in company_names:
    print(i.text)
    data = i.text
    output_company_names.append(data)

len(output_company_names) #100
output_company_names[2]

# Get dates of each job posting
dates = soup.find_all('p', class_='is-small has-text-grey')
output_dates = []
for i in dates:
    data = i.text
    data = data.strip() # removes empty space on either side of text
    data = data.replace('\n', '') # removes empty lines
    data = data.replace(' ', '') # removes empty spaces
    output_dates.append(data)

len(output_dates) # 100

# Get descriptions of each articlefind each article where class='Box-row'
locations = soup.find_all('p', class_='location')
output_locations = []
for i in locations:
    print(i.text)
    data = i.text
    data = data.strip() 
    output_locations.append(data)

len(output_locations) #100
output_locations[8]


# Compile data into a new dataframe
df = pd.DataFrame({'jobtitles':output_job_titles,'companies':output_company_names, 'dates':output_dates})
# Export to new csv 
df.to_csv('data/fake_job_board.csv')