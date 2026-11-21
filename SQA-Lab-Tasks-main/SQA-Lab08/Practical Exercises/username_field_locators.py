from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    username = driver.find_element(By.ID, "my-text-id")
    print("Located using ID:", username.get_attribute("id"))

    username = driver.find_element(By.NAME, "my-text")
    print("Located using Name:", username.get_attribute("name"))

finally:
    driver.quit()
    print("Browser closed.")