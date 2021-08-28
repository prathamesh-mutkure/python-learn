from selenium import webdriver

url = "http://secure-retreat-92358.herokuapp.com/"
driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get(url)

f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
submit = driver.find_element_by_class_name("btn")

f_name.send_keys("Prathamesh")
l_name.send_keys("Mutkure")
email.send_keys("prathamesh@mutkure.com")
submit.click()

driver.close()
driver.quit()
