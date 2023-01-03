import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/")

# find CheckBox 
driver.find_element(By.CSS_SELECTOR , '#content > ul > li:nth-child(6) > a').click()

# click checkbox 1
driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()

# click checkbox 2
driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()

