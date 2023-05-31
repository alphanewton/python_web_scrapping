from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#THIS ONE DISLIKES ALL MATCHES

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

driver_path = "/Users/newto/Documents/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://tinder.com/")
driver.maximize_window()

sleep(3)
agreement_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
agreement_button.click()

sleep(3)
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
login_button.click()

sleep(3)
facebook_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div")
facebook_button.click()

sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(3)
email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

sleep(3)
driver.switch_to.window(base_window)
print(driver.title)

sleep(3)

allow_location_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")
allow_location_button.click()

sleep(1)
notifications_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
notifications_button.click()

for n in range(100):
    sleep(1)
    try:
        print("Disliked")
        sleep(10)
        body = driver.find_element(By.CSS_SELECTOR, "body")
        body.send_keys(Keys.LEFT)
    except ElementClickInterceptedException:
        sleep(2)
        pass

driver.quit()
