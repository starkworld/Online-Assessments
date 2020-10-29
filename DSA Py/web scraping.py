import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# hitting link
page = requests.get(URL)
# getting content of page
soup = BeautifulSoup(page.content, 'html.parser')
# finding specific content of page by ID
results = soup.find(id='ResultsContainer')
# finding content by class
job_elem = results.findAll('section', class_='card-content')

# Converting HTML content to text
for job_ele in job_elem:
    title = job_ele.find('h2', class_='title')
    company = job_ele.find('div', class_='company')
    loc = job_ele.find('div', class_='location')
    if None in (title, company, loc):
        continue
    print(title.text.strip(), company.text.strip(), loc.text.strip())

# extract attributes from HTML Elements
python_jobs = results.find_all('h2', string=lambda text: 'Python' in text)
for p_jobs in python_jobs:
    link = p_jobs.find('a')['href']
    print(p_jobs.text.strip())
    print(f'Apply here: {link}\n')


# print(results.prettify())

# Credits: RealPython

