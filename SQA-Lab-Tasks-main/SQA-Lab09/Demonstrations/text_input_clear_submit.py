
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    search = wait.until(
        EC.element_to_be_clickable((By.ID, "my-text-id"))
    )

    print("Web form opened.")

    search.send_keys("Selenium WebDriver tutorial")
    print("First text entered:", search.get_attribute("value"))

    search.clear()
    print("Field cleared:", search.get_attribute("value"))

    search.send_keys("Software Quality Engineering")
    print("Second text entered:", search.get_attribute("value"))

    search.send_keys(Keys.RETURN)

    print("Enter key pressed.")

finally:
    driver.quit()
    print("Browser closed.")
