from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


INSTA_USER_NAME = os.getenv("INSTA_USER_NAME")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")
INSTA_PROFILE = os.getenv("INSTA_PROFILE")

url = "https://www.instagram.com/"
web_driver_path = "/Users/prathamesh/Developer/chrome/chromedriver"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=web_driver_path)

    def login(self):
        self.driver.get(INSTA_PROFILE)
        sleep(3)

        # log_in_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
        # log_in_btn.click()
        # sleep(3)

        user_name_field = self.driver.find_element_by_name("username")
        password_field = self.driver.find_element_by_name("password")

        user_name_field.send_keys(INSTA_USER_NAME)
        password_field.send_keys(INSTA_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        sleep(3)
        save_info_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_info_btn.click()

        sleep(3)
        not_now_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now_btn.click()

        sleep(1)
        self.driver.get(INSTA_PROFILE)

        sleep(5)

    def find_followers(self):
        followers_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()

        sleep(5)
        div_container = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_container)
            sleep(3)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li .sqdOP.L3NKy.y3zKF")

        for follow_button in follow_buttons:
            sleep(1)

            if follow_button.text == "Follow":
                follow_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
