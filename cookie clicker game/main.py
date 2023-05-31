from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver_path = "/Users/newto/Documents/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

clicker = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + (60*5)


while True:
    clicker.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            if price.text != "":
                cost = int(price.text.strip().split("-")[1].replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        curr_cookies = driver.find_element(By.ID, "money").text.replace(",", "")
        cookie_count = int(curr_cookies)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable = max(affordable_upgrades)
        print(highest_price_affordable)
        to_purchase_id = affordable_upgrades[highest_price_affordable]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > timeout:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

