from selenium import webdriver
from time import sleep

url = "https://orteil.dashnet.org/cookieclicker/"
driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get(url)
cookie = driver.find_element_by_id("bigCookie")


def buy_items():
    store_items = driver.find_elements_by_css_selector(".product.unlocked.enabled")
    most_expensive_item = store_items[len(store_items) - 1]
    most_expensive_item.click()


counter = 0
while True:
    sleep(0.01)

    cookie.click()
    counter += 1

    if counter > 500:
        counter = 0
        buy_items()
