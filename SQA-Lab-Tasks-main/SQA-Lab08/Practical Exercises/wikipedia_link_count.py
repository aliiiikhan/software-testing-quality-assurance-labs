from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.wikipedia.org/")

    print("Page Title:", driver.title)

    links = driver.find_elements(By.TAG_NAME, "a")

    print("Total links found:", len(links))

finally:
    driver.quit()
    print("Browser closed.")