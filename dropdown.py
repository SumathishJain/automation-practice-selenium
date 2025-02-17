from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
url = "https://the-internet.herokuapp.com/"
driver.get(url)
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Dropdown").click()
time.sleep(3)
dropdown_element = driver.find_element(By.ID, "dropdown")  
select = Select(dropdown_element)  # this Select class is used to select the options from dropdown

# There are three different ways to select an option from a dropdown
# 1. select the option by its visible text

# select.select_by_visible_text("Option 2")
# time.sleep(3)


# 2. select the option by its index

# select.select_by_index(1) # index value starts by 0 and if we provide o as the value, first option will be selected (first option includes header of the dropdown)
# time.sleep(3)


# 3. select the option by its value

# select.select_by_value("2")  # value fo the option present in the html code.
# time.sleep(3)



# test case 1 :  Verify whether the expected count of the dropdown is equal to actual count of dropdowns

# actual_count = len(select.options)
# expected_count = 3

# if actual_count == expected_count:  
#     print(f"Test case passed. Except count {expected_count} is equal to Actual count {actual_count}.")
# else:
#     print(f"Test case failed. Except count {expected_count} is equal to Actual count {actual_count}.")



# test case 2 :  Verify whether the expected option is present in the dropdown list. if contains, select the option else, don't select.

# expected_option = "Option 2"
# for option in select.options:
#     if option.text == expected_option:
#         option.click()
#         time.sleep(3)
#         print("Clicked on expected option ", expected_option)
#         break
#     else:
#         print("Expected option not found.", expected_option)
        