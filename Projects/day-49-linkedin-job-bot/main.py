from selenium import webdriver
from time import sleep
import os

USERNAME = os.getenv("LINKEDIN_USERNAME")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

url = "https://www.linkedin.com/jobs/search?keywords=Flutter&location=Nagpur%2C%2BMaharashtra%2C%2BIndia&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=2692215053&position=2&pageNum=0"
driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get(url)
sleep(2)

sign_in_btn = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_in_btn.click()

email_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")
sign_in_btn = driver.find_element_by_css_selector(".btn__primary--large.from__button--floating")

email_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
sign_in_btn.click()

# driver.close()
# driver.quit()
