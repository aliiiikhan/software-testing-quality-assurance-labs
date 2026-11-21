from selenium import webdriver

# Launch Chrome
driver = webdriver.Chrome()

# Open a test website
driver.get("https://www.google.com")

# Print browser information
print("Browser launched successfully!")
print("Page title:", driver.title)
print("Current URL:", driver.current_url)

# Close browser
driver.quit()