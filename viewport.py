from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

viewports = [(1024,768), (786,1024), (375,667), (414, 896)]

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# driver.set_window_size(786, 1024)
# time.sleep(6)

#            or

try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(6)

finally:
    driver.close()