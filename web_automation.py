import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://linkedin.com/")
driver.maximize_window()

time.sleep(2)

emailInput = driver.find_element(By.XPATH, '//*[@id="session_key"]')
emailInput.click()
emailInput.send_keys(config('LINKEDIN_EMAIL'))

passwordInput = driver.find_element(By.XPATH, '//*[@id="session_password"]')
passwordInput.click()
passwordInput.send_keys(config('LINKEDIN_PASSWORD'))

time.sleep(2)
submitBtn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button').click()

time.sleep(2)
gotoProfile = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a').click()
