import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver_path = "/Users/newto/Documents/chromedriver_mac_arm64/chromedriver"

ISP_NAME = "NKN Core Network"
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        go_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go_button.click()

        time.sleep(60)

        download = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        upload = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.down = float(download.text)
        self.up = float(upload.text)

        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.maximize_window()

        time.sleep(3)
        username = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        # time.sleep(30)
        #
        # #TWITTER VERIFICATION THAT U HAVE TO DO IN 30 SEC!
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        tweet_button.click()

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_textarea = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_textarea.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
        tweet_button.click()

        time.sleep(5)
        self.driver.quit()


newbot = InternetSpeedTwitterBot()
# newbot.get_internet_speed()
newbot.tweet_at_provider()
