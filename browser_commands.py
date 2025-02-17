from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print('window maximized')
time.sleep(10)
driver.minimize_window()
print('window minimized')
time.sleep(3)
driver.fullscreen_window()
print('window full screen')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(10)
reset_password = driver.find_element(By.CSS_SELECTOR, '.oxd-text.oxd-text--h6.orangehrm-forgot-password-title')
assert reset_password.text ==  "Reset Password"
print('clicked on forgot password')
time.sleep(3)
driver.back()
print('window backwarded')
time.sleep(3)
driver.forward()
print('window forwarded')
time.sleep(3)
driver.refresh()
print('window refreshed')
time.sleep(3)
driver.close()
