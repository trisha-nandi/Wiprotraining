import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
browser = input("Enter the browser name: ")

match browser:
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case _:
        print('Enter the correct browser name !!')

driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle=='Google':
    print("Google Homepage loaded - Pass")
else:
    print("Google Homepage NOT loaded - Fail")

time.sleep(10)
driver.quit()