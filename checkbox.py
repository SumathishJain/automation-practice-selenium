from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# to check the specific checkbox, use this way
# driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()
# time.sleep(3)



# to check all the checkboxes at a time by pressing SPACE BAR, use this way

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
time.sleep(3)



checked_count = 0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

expected_checked_count = 7

if checked_count == expected_checked_count:
    print("checkbox count satisfied.\n expected count = ",expected_checked_count,"\n actual count =  ", checked_count)
else:
    print("checkbox count not satisfied.\n expected count = ",expected_checked_count,"\n actual count =  ", checked_count)

time.sleep(5)
driver.close()



