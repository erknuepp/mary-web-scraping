from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep

path = r"C:\WebDrivers\chromedriver.exe"  # Put the path to your Chromedriver
s = Service(path)
driver = wd.Chrome(service=s)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
url = 'https://www.immobilienscout24.at/regional/wien/wien/wohnung-mieten'
driver.get(url)
sleep(2)
# React Slider Button
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "SzJj7")))  
els = driver.find_elements(By.XPATH, '//a[contains(@href,"expose")]')

for el in els:
    print(el.get_attribute("href"))

driver.quit()
