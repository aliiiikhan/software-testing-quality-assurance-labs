
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    wait = WebDriverWait(driver, 15)

    # Open registration form
    driver.get("https://demoqa.com/automation-practice-form")

    # Enter first name
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name.send_keys("Abdul")

    # Enter last name
    driver.find_element(By.ID, "lastName").send_keys("Qadir")

    # Enter email
    driver.find_element(By.ID, "userEmail").send_keys(
        "abdul.test@example.com"
    )

    # Select gender using its label
    driver.find_element(
        By.XPATH, "//label[@for='gender-radio-1']"
    ).click()

    # Enter mobile number
    driver.find_element(By.ID, "userNumber").send_keys("03001234567")

    # Verify entered values
    print("First Name:", first_name.get_attribute("value"))
    print("Last Name:", driver.find_element(By.ID, "lastName").get_attribute("value"))
    print("Email:", driver.find_element(By.ID, "userEmail").get_attribute("value"))
    print("Gender Selected:", driver.find_element(By.ID, "gender-radio-1").is_selected())
    print("Mobile:", driver.find_element(By.ID, "userNumber").get_attribute("value"))

finally:
    driver.quit()
    print("Browser closed.")
