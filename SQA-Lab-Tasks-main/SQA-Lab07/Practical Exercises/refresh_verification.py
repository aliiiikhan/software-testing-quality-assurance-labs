
from selenium import webdriver
import time

# Start Firefox browser
driver = webdriver.Firefox()
driver.maximize_window()

# Open Python website
driver.get("https://www.python.org")
time.sleep(3)

# Store title before refresh
title_before = driver.title
print("Title Before Refresh:", title_before)

# Refresh the page
driver.refresh()
time.sleep(3)

# Store title after refresh
title_after = driver.title
print("Title After Refresh:", title_after)

# Compare both titles
if title_before == title_after:
    print("\nResult: Title remained the same after refresh.")
else:
    print("\nResult: Title changed after refresh.")

# Close browser
driver.quit()
print("Browser session closed.")
