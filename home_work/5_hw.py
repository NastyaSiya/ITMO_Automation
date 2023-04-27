from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

icon = driver.find_element(By.CSS_SELECTOR, '#user-name'),\
    driver.find_element(By.CSS_SELECTOR, '#password'),\
    driver.find_element(By.CSS_SELECTOR, '#login-button')
# na saite net knopki submit, rabotaet tolko v polozhitelnom sluchae
if icon is None:
    print('Elementy ne naideny')
else:
    print('Elementy naideny')
