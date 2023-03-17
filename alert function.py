from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#chrome path
driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")

#website link
driver.get("https://letcode.in/windows")


driver.find_element(By.XPATH,"//button[@id='home']").click()

#switch function with single alert function
windo=driver.find_element(By.XPATH,"//button[@id='accept']")
windo.click()
driver.switch_to.alert.accept()

#alert accept or dismess function
driver.find_element(By.XPATH,"//button[@id='confirm']").click()
driver.switch_to.alert.accept()

#alert with send keys function
driver.find_element(By.XPATH,"//button[@id='prompt']").click()
name=driver.switch_to.alert
name.send_keys("hi")
name.accept()

driver.close()