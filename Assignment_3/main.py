# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the cibc home page
driver.get("https://www.cibc.com/")
time.sleep(4)

# Selecting credit card services from the home page
credit_card = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div/nav/section/ul/li[2]/a")
credit_card.click()
time.sleep(4)


# Selecting the type of credit card service required
student_service = driver.find_element("id","buttonid-1649344612028")
student_service.click()
time.sleep(5)

# Selecting a card from the list of student cards provided
select_card = driver.find_element("xpath","/html/body/div[1]/div[1]/main/div[5]/div[2]/div[2]/div[3]/div[3]/div/div[1]/div/div[1]/h3/a")
select_card.click()
time.sleep(5)

# Clicking on Apply for card
apply = driver.find_element("id","button-1646237575398")
apply.click()
time.sleep(5)

# Closing the webdriver
driver.close()