from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/")

driver.find_element(By.LINK_TEXT, 'JavaScript Alerts').click()
#Click Button JS Alerts
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()

time.sleep(2)
#Click on Alert OK
driver.switch_to.alert.accept()

time.sleep(2)

#Click Button JS Confirm
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()

time.sleep(2)
#Click on Alert Ok
driver.switch_to.alert.accept()

time.sleep(2)

#Click Button JS Confirm
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()

time.sleep(2)
#Click on Alert Cancel
driver.switch_to.alert.dismiss()


time.sleep(2)

#Click Button JS Prompt (send Text)
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()

time.sleep(2)
#Typing on Alert 
driver.switch_to.alert.send_keys('Hola Amigos!')

time.sleep(2)
#Click on Alert Ok

driver.switch_to.alert.accept()


time.sleep(3)