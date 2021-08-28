from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get(url)

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# article_count.click()

search_bar = driver.find_element_by_name("search")
search_bar.send_keys("Selenium")
search_bar.send_keys(Keys.ENTER)


driver.close()
driver.quit()
