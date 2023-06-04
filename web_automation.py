import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = Options()

# Run Chrome in detached mode
options.add_experimental_option("detach", True)

# Disable logging
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the LinkedIn website
driver.get("https://linkedin.com/")

# Maximize the browser window
driver.maximize_window()

# Wait for 2 seconds
time.sleep(2)

# Find the email input field and enter the LinkedIn email from the config file
emailInput = driver.find_element(By.XPATH, '//*[@id="session_key"]')
emailInput.click()
emailInput.send_keys(config('LINKEDIN_EMAIL'))

# Find the password input field and enter the LinkedIn password from the config file
passwordInput = driver.find_element(By.XPATH, '//*[@id="session_password"]')
passwordInput.click()
passwordInput.send_keys(config('LINKEDIN_PASSWORD'))

time.sleep(2)

# Find and click the submit button to log in
submitBtn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click()



time.sleep(2)

# Find and click the profile link to go to the user's profile
gotoProfile = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a').click()
