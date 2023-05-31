import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.88497916322538%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.665441766568215%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D", headers=headers)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

all_address_elements = soup.select(".property-card-data address")
all_addresses = [address.getText().split(' | ')[-1] for address in all_address_elements]

all_price_elements = soup.select(".property-card-data span")
all_prices = []
for price in all_price_elements:
    price = price.getText()
    if "+" in price:
        all_prices.append(price.split("+")[0])
    else:
        all_prices.append(price.split("/")[0])

all_link_elements = soup.select(".property-card-data a")
all_links = []
for url in all_link_elements:
    link = url["href"]
    if "http" not in link:
        all_links.append(f"http://www.zillow.com{link}")
    else:
        all_links.append(link)


driver_path = "/Users/newto/Documents/chromedriver_mac_arm64/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)

for i in range(len(all_addresses)):
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScOeRj_w6smKNCTE1VGr4GCZM36iZrGpWvJjg2lCcrwT-iA2g/viewform?usp=sf_link")
    sleep(2)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(all_addresses[i])

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(all_prices[i])

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(all_links[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()