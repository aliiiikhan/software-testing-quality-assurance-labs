import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://google.com")
print(driver.title)
time.sleep(3)

driver.get("https://youtube.com")
print(driver.title)
time.sleep(3)

driver.back()
print(driver.title)
time.sleep(3)

driver.forward()
print(driver.title)
time.sleep(3)

driver.switch_to.new_window("tab")
driver.get("https://wikipedia.org")
time.sleep(3)

driver.close()
time.sleep(3)

driver.quit()

#clas work
#get.google.com
# search.send_keys("software testing and quality assurance")
#search.send_keys(Keys.RETURN)
#google search box m jae wsaha input likha fir oska erase krka doabra new search krda
#ya pora automated hu code ks ath time duration b hu oska sath
