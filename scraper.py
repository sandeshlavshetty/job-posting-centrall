from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

job_site_url='https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'
#the changes hbbvh
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--no-sandbox')
  driver = webdriver.Chrome(options=chrome_options)
  return driver




# if __name__ == "__main__":
print('Creating driver')
driver = get_driver()
  
print('fetching the page')
wait.WebDriverWait(driver, 10)
driver.get(job_site_url)
print('Page title:',driver.title)

print('get the page class')
job_li='clearfix job-bx wht-shd-bx'


jobs = driver.find_elements(By.CLASS_NAME, job_li)
print(f'found {len(jobs)} jobs')