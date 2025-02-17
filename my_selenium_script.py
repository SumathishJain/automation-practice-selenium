from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
search = driver.find_element(By.NAME,'q')
search.clear()
search.send_keys('speed test')
search.send_keys(Keys.RETURN)
time.sleep(6)
search.find_element(By.ID, 'knowledge-verticals-internetspeedtest__test_button')
search.click()
time.sleep(6)
driver.close()