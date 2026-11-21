
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate checkboxes
    checkbox1 = driver.find_element(By.ID, "my-check-1")
    checkbox2 = driver.find_element(By.ID, "my-check-2")

    print("Initial Checkbox 1:", checkbox1.is_selected())
    print("Initial Checkbox 2:", checkbox2.is_selected())

    # Select Checkbox 2
    if not checkbox2.is_selected():
        checkbox2.click()

    print("After clicking Checkbox 2:", checkbox2.is_selected())

    # Locate radio buttons
    radio1 = driver.find_element(By.ID, "my-radio-1")
    radio2 = driver.find_element(By.ID, "my-radio-2")

    print("\nInitial Radio 1:", radio1.is_selected())
    print("Initial Radio 2:", radio2.is_selected())

    # Select Radio 2
    radio2.click()

    print("\nAfter clicking Radio 2:")
    print("Radio 1:", radio1.is_selected())
    print("Radio 2:", radio2.is_selected())

finally:
    driver.quit()
    print("\nBrowser closed.")
