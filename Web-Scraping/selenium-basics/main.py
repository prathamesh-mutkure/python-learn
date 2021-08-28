from selenium import webdriver


def print_data(tag, data):
    print(tag + " : " + str(data))


url = "https://www.python.org/"
chrome_driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=url)

print_data("find_element_by_name", driver.find_element_by_name("q").get_attribute("placeholder"))
print_data("find_element_by_id", driver.find_element_by_id("submit").get_attribute("title"))
print_data("find_element_by_xpath", driver.find_element_by_xpath('//*[@id="start-shell"]/span').get_attribute("class"))
print_data("find_element_by_css_selector", driver.find_element_by_css_selector(".download-widget h2").text)
print_data("find_elements_by_css_selector", driver.find_elements_by_css_selector(".download-widget p")[0].text)

driver.close()
driver.quit()
