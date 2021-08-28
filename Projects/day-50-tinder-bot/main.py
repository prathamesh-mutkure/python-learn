from selenium import webdriver
from time import sleep
import os

url = "https://tinder.com/"
driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get(url)
sleep(1)

sign_in_btn = driver.find_element_by_xpath('//*[@id="t812761606"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
sign_in_btn.click()


# driver.close()
# driver.quit()
