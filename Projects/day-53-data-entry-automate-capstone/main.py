from selenium import webdriver
from time import sleep


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc89VH_WUNlpw04IcLRpeKgr0rKe_BUCkPTUCx9LJFkYYdbmA/viewform"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
web_driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"


class DataEntryBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=web_driver_path)
        self.price_list = []
        self.address_list = []
        self.link_list = []
        self.properties = 0

    def get_zillow_listings(self):
        self.driver.get(ZILLOW_URL)
        sleep(10)

        pricing_tags = self.driver.find_elements_by_css_selector(".list-card-info .list-card-price")
        address_tags = self.driver.find_elements_by_css_selector(".list-card-info .list-card-addr")
        link_tags = self.driver.find_elements_by_css_selector(".list-card-info a")

        self.price_list = [(price_tag.text.split("/")[0]).split("+")[0] for price_tag in pricing_tags]
        self.address_list = [address_tag.text for address_tag in address_tags]
        self.link_list = [link_tag.get_attribute("href") for link_tag in link_tags]
        self.properties = len(self.price_list)

    def fill_form(self):
        self.driver.get(FORM_URL)

        for i in range(self.properties):
            sleep(1)

            address_field = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_btn = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

            address_field.send_keys(self.address_list[i])
            price_field.send_keys(self.price_list[i])
            link_field.send_keys(self.link_list[i])
            submit_btn.click()

            sleep(1)
            another_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_btn.click()


bot = DataEntryBot()
bot.get_zillow_listings()
bot.fill_form()
