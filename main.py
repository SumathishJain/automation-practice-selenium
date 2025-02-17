# Selenium is an open-source automation testing framework used for testing web applications across different browsers and operating systems

# Selenium WebDriver is a crucial part of Selenium that provides an interface to interact with web browsers. It controls browsers natively using their automation engines, ensuring real-time user-like interaction.

# from selenium import webdriver  # 
# from selenium.webdriver.common.keys import Keys  # Keys was imported so that we can use keys.return
# from selenium.webdriver.common.by import By  # By is imported so that we can find the element By using it's name, id, class 
# import time

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.ID, "id-search-field")
# elem.clear()
# elem.send_keys("Python")  # send_keys used to send anything
# elem.send_keys(Keys.RETURN)  # Keys.RETURN is used to click enter
# assert "No results found." not in driver.page_source
# time.sleep(6)  # It will wait for 6 secs before the next step i.e, driver.close()
# driver.close()

# <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="Python" tabindex="1">




# from selenium import webdriver
# import time


# browser = webdriver.Chrome()
# browser.get("https://selenium.dev/")
# browser.maximize_window()  # to maximize the size of the browser
# title = browser.title  # to get the title of the web page we use title method because title of the webpage will be written inside title tag under head section
# print(title)
# assert "Selenium" in title  # to do assertion against expected vs actual output
# time.sleep(6)




# --------------------------------------------------- ------- elements and locators ----------------------------------- ----------------------- 
