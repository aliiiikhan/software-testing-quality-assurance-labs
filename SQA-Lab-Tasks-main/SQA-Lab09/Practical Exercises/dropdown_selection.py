
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate the dropdown
    dropdown_element = driver.find_element(By.NAME, "my-select")
    dropdown = Select(dropdown_element)

    # Select by visible text
    dropdown.select_by_visible_text("Two")
    print("Selected by visible text:", dropdown.first_selected_option.text)

    # Select by index
    dropdown.select_by_index(1)
    print("Selected by index:", dropdown.first_selected_option.text)

    # Select by value
    dropdown.select_by_value("3")
    print("Selected by value:", dropdown.first_selected_option.text)

finally:
    driver.quit()
    print("Browser closed.")
