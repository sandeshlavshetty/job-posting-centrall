import requests
from bs4 import BeautifulSoup
job_site_url='https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'

#does not execute javascript
response = requests.get(job_site_url)

print('Status Code:', response.status_code)

with open('trending.html', 'w') as f:
    f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

print('Page title:',doc.title.text)

#find all job li tags 
job_li = doc.find_all('li',class_='clearfix job-bx wht-shd-bx')

print(f'found {len(job_li)} jobs')

