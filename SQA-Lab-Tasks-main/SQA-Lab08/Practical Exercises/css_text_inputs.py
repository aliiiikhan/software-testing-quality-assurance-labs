from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_inputs = driver.find_elements(
        By.CSS_SELECTOR,
        "input[type='text']"
    )

    print("Total text input fields:", len(text_inputs))

    for field in text_inputs:
        print(
            "ID:", field.get_attribute("id"),
            "| Name:", field.get_attribute("name")
        )

finally:
    driver.quit()
    print("Browser closed.")