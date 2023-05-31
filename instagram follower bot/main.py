from selenium import webdriver
import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = 'chefsteps'
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'

driver_path = '/Users/newto/Documents/chromedriver_mac_arm64/chromedriver'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)

        username_input = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        skip_popup = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        skip_popup.click()
        time.sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)
        modal = self.driver.find_element(By.CLASS_NAME, "_aano")

        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div._aano button")
        print(f"Found {len(all_buttons)} buttons")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")
                cancel_button.click()

newsta = InstaFollower()
newsta.login()
newsta.find_followers()
newsta.follow()