import time
from turtle import forward

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5) 
driver.get("https://youtube.com")
time.sleep(5)  
driver.back()
time.sleep(5)  
driver.forward()
time.sleep(5)  
driver.quit()