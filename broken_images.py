from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Broken Images").click()
# time.sleep(3)

all_image_link = driver.find_elements(By.TAG_NAME, "img")
print({len(all_image_link)})
broken_images = []

for image in all_image_link:
    src = image.get_attribute('src')
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found")

if broken_images:
    print("List of broken images.")
    for broken_image in broken_images:
        print(broken_image)

else:
    print("No Broken Image found")