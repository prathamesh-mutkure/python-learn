from selenium import webdriver

url = "https://www.python.org/"
chrome_driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=url)

event_lists = driver.find_elements_by_css_selector(".event-widget .shrubbery ul.menu li")
events = {}

for i in range(len(event_lists)):
    event = event_lists[i]
    time, name = event.text.split("\n")
    events[i] = {
        "time": time,
        "name": name,
    }


print(events)


driver.close()
driver.quit()
