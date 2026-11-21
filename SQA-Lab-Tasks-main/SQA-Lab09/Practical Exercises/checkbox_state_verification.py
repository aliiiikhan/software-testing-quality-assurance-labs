
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate checkbox
    checkbox = driver.find_element(By.ID, "my-check-1")

    # Record initial state
    initial_state = checkbox.is_selected()
    print("Initial checkbox state:", initial_state)

    # First click
    checkbox.click()
    after_first_click = checkbox.is_selected()
    print("After first click:", after_first_click)

    # Second click
    checkbox.click()
    after_second_click = checkbox.is_selected()
    print("After second click:", after_second_click)

    # Verify original state is restored
    print("Original state restored:", initial_state == after_second_click)

finally:
    driver.quit()
    print("Browser closed.")
