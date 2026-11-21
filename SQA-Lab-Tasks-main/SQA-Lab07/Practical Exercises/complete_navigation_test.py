from selenium import webdriver
import time

# Start Firefox browser
driver = webdriver.Firefox()
driver.maximize_window()

# Open first website
driver.get("https://www.google.com")
print("First Website:")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Navigate to second website
driver.get("https://www.python.org")
print("\nSecond Website:")
print("Title:", driver.title)
print("URL:", driver.current_url)
time.sleep(2)

# Go back
driver.back()
time.sleep(2)
print("\nAfter Back:")
print("Title:", driver.title)

# Go forward
driver.forward()
time.sleep(2)
print("\nAfter Forward:")
print("Title:", driver.title)

# Refresh current page
driver.refresh()
time.sleep(3)
print("\nAfter Refresh:")
print("Title:", driver.title)

# Close browser
driver.quit()
print("\nBrowser session closed.")