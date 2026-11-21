from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/html/html_tables.asp")

    cell = driver.find_element(
        By.XPATH,
        "//table[@id='customers']//tr[2]/td[1]"
    )

    print("Located table cell using XPath:", cell.text)

finally:
    driver.quit()
    print("Browser closed.")