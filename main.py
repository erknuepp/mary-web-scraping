from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

path = r"C:\WebDrivers\chromedriver.exe" # Put the path to your Chromedriver
s = Service(path)
driver = wd.Chrome(service=s)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('https://www.immobilienscout24.at/regional/wien/wien/wohnung-mieten')
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "SzJj7"))) # React Slider Button
els = driver.find_elements(By.XPATH, '//a[contains(@href,"expose")]')

for el in els:
    print(el.get_attribute("href"))

driver.quit()