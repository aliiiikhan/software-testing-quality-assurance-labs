
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate both radio buttons
    radio1 = driver.find_element(By.ID, "my-radio-1")
    radio2 = driver.find_element(By.ID, "my-radio-2")

    # Check initial states
    print("Initial Radio 1:", radio1.is_selected())
    print("Initial Radio 2:", radio2.is_selected())

    # Select Radio 2
    radio2.click()

    print("\nAfter selecting Radio 2:")
    print("Radio 1:", radio1.is_selected())
    print("Radio 2:", radio2.is_selected())

    # Select Radio 1
    radio1.click()

    print("\nAfter selecting Radio 1:")
    print("Radio 1:", radio1.is_selected())
    print("Radio 2:", radio2.is_selected())

finally:
    driver.quit()
    print("\nBrowser closed.")
