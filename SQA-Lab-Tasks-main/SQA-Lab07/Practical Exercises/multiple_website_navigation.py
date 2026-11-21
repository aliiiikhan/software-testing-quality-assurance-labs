
from selenium import webdriver
import time

# Start Firefox browser
driver = webdriver.Firefox()
driver.maximize_window()

# Open first website
driver.get("https://www.google.com")
print("Website 1:", driver.title)
print("URL 1:", driver.current_url)

time.sleep(2)

# Open second website
driver.get("https://www.python.org")
print("\nWebsite 2:", driver.title)
print("URL 2:", driver.current_url)

time.sleep(2)

# Open third website
driver.get("https://www.wikipedia.org")
print("\nWebsite 3:", driver.title)
print("URL 3:", driver.current_url)

time.sleep(2)

# Go back twice
driver.back()
time.sleep(2)

driver.back()
time.sleep(2)

print("\nAfter Back Twice:")
print("Title:", driver.title)
print("URL:", driver.current_url)

# Go forward once
driver.forward()
time.sleep(2)

print("\nAfter Forward Once:")
print("Title:", driver.title)
print("URL:", driver.current_url)

# Close browser
driver.quit()
print("\nBrowser session closed.")
