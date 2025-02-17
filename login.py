from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"

driver.get(login_url)

username_field = driver.find_element(By.ID, 'user-name')
password_field = driver.find_element(By.ID, 'password')

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, 'login-button')
assert not login_button.get_attribute("disabled")
time.sleep(3)

login_button.click()
login_success_element = driver.find_element(By.CSS_SELECTOR, ".title")
assert login_success_element.text == "Products"
time.sleep(6)