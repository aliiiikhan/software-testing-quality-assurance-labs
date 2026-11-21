
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    print("Page Title:", driver.title)

    # 1. ID locator
    element_id = driver.find_element(By.ID, "my-text-id")
    print("Found by ID:", element_id.get_attribute("id"))

    # 2. Name locator
    element_name = driver.find_element(By.NAME, "my-text")
    print("Found by Name:", element_name.get_attribute("name"))

    # 3. Class Name locator
    element_class = driver.find_element(By.CLASS_NAME, "form-control")
    print("Found by Class Name:", element_class.get_attribute("class"))

    # 4. Tag Name locator
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print("Total input elements:", len(inputs))

    # 5. CSS Selector
    button = driver.find_element(By.CSS_SELECTOR, "button")
    print("Found by CSS Selector:", button.text)

finally:
    driver.quit()
    print("Browser closed successfully.")
