from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.dailymail.co.uk/home/index.html"
path = "/Users/newto/Downloads/chromedriver_mac_arm64"

service = Service(executable_path=path)
driver = webdriver.Chrome(service= service)
driver.get(website)