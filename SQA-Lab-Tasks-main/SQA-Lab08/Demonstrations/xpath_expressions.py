
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    print("Page Title:", driver.title)

    print("\n--- INPUT ELEMENTS ---")

    inputs = driver.find_elements(By.TAG_NAME, "input")

    for item in inputs:
        print(
            "ID:", item.get_attribute("id"),
            "| Name:", item.get_attribute("name"),
            "| Type:", item.get_attribute("type")
        )

    print("\n--- BUTTON ELEMENTS ---")

    buttons = driver.find_elements(By.TAG_NAME, "button")

    for item in buttons:
        print(
            "Text:", item.text,
            "| Type:", item.get_attribute("type")
        )

finally:
    driver.quit()
    print("\nBrowser closed.")
