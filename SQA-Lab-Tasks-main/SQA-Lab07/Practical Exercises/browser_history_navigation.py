
from selenium import webdriver
import time

# Start Firefox browser
driver = webdriver.Firefox()
driver.maximize_window()

# Open first website
driver.get("https://www.google.com")
print("First Page:", driver.title)

time.sleep(2)

# Open second website
driver.get("https://www.python.org")
print("Second Page:", driver.title)

time.sleep(2)

# Open third website
driver.get("https://www.wikipedia.org")
print("Third Page:", driver.title)

time.sleep(2)

# Go back twice
driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

print("\nAfter Going Back Twice:")
print("Current Title:", driver.title)

# Go forward once
driver.forward()
time.sleep(2)

print("\nAfter Going Forward Once:")
print("Current Title:", driver.title)

# Close browser
driver.quit()
print("\nBrowser session closed.")
