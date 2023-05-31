import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"


driver_path = "/Users/newto/Documents/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3548917165&distance=25&f_AL=true&f_E=1&f_JT=I&f_WT=2&geoId=92000000&keywords=python&location=Worldwide&refresh=true&sortBy=R")

login_button = driver.find_element(By.LINK_TEXT, "Sign in")
login_button.click()

username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# SECURITY CHECK BY LINKEDIN WHICH YOU NEED TO MANUALLY ENTER! Could fail
time.sleep(40)


all_jobs = driver.find_elements(By.CLASS_NAME, "jobs-search__results-list")
for job in all_jobs:
    job.click()
    time.sleep(2)

    try:
        
        #save_button = driver.find_element(By.LINK_TEXT, "Save")
        # save_button.click()

        apply_button = driver.find_element(By.CLASS_NAME, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone_text = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        if phone_text == '':
            phone_text.send_keys("55087030")

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application skipped")
            continue
        else:
            submit_button.click()

    except NoSuchElementException:
        print("No submit button")
        continue

time.sleep(5)
driver.quit()

