import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://jqueryui.com/"
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"total number of links on the page: {len(all_links)}")
# time.sleep(3)

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken Links: {href} Status code: {response.status_code}")

driver.quit()


