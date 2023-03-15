import time
import openpyxl
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

time.sleep(3)

# login with credentials

loginUser = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
loginUser.click()
loginUser.send_keys(config('HRM_USERNAME'))

loginPassword = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
loginPassword.click()
loginPassword.send_keys(config('HRM_PASSWORD'))

loginBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
loginBtn.click()

# Goto admin panel 
time.sleep(2)
adminPanel = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

# Read data from excel
excelSheet = openpyxl.load_workbook('./userdata.xlsx')
activeSheet = excelSheet.active
time.sleep(2)
for row in range(2,8):
    userName = activeSheet['A'+str(row)].value
    userUser = activeSheet['B'+str(row)].value
    userPass = activeSheet['C'+str(row)].value

    if(userName == 'None' or userUser == 'None' or userPass == 'None' ):
        print('Data is Empty or Insufficient data!')
        continue

    try:

        addUserBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()

        time.sleep(2)
        # select user role
        openUserDropDown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div')
        openUserDropDown.click()
        time.sleep(5)
        # select status
        openStatusDropDown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div')
        openStatusDropDown.click()
        time.sleep(5)
        # select user
        openNameDropDown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input')
        openNameDropDown.click()
        openNameDropDown.send_keys(userName)
        time.sleep(8)

        #create username
        openNameDropDown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input')
        openNameDropDown.click()
        openNameDropDown.send_keys(userUser)

        #create password
        openNameDropDown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
        openNameDropDown.click()
        openNameDropDown.send_keys(userPass)

        #create confirm password
        openNameDropDown = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
        openNameDropDown.click()
        openNameDropDown.send_keys(userPass)

        time.sleep(3)
        #save user
        saveUserBtn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()

        time.sleep(10)

    except:
        # save the status in woorkbook
        activeSheet['D'+ str(row)].value = "failed"
        excelSheet.save("userdata.xlsx")
        continue

    else:
        # save the status in woorkbook
        activeSheet['D'+ str(row)].value = "created"
        excelSheet.save("userdata.xlsx")

# close the current window
driver.close()





