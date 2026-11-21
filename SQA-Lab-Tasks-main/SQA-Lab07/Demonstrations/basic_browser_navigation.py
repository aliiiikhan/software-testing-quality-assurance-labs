
from selenium import webdriver
import time

# Start Firefox browser
driver = webdriver.Firefox()

# Open Google
driver.get("https://www.google.com")
print("Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(3)

# Navigate to Wikipedia
driver.get("https://www.wikipedia.org")
print("Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(3)

# Go Back
driver.back()
print("After Back:", driver.title)

time.sleep(3)

# Go Forward
driver.forward()
print("After Forward:", driver.title)

time.sleep(3)

# Refresh the page
driver.refresh()
print("After Refresh:", driver.title)

time.sleep(3)

# Close browser session
driver.quit()
print("Browser session closed.")
