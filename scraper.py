import requests

job_site_url='https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'

response = requests.get(job_site_url)

print('Status Code:', response.status_code)

with open('trending.html', 'w') as f:
    f.write(response.text)