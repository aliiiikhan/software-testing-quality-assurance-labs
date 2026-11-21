
from selenium import webdriver
import time

# Start Firefox browser
driver = webdriver.Firefox()

# Maximize browser window
driver.maximize_window()

# Open Python website
driver.get("https://www.python.org")

time.sleep(3)

# Read current page information
print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

time.sleep(3)

# Close browser
driver.quit()
print("Browser session closed.")
