import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Windows\chromedriver_win32\chromedriver.exe')

#Variables
username = "michaelbblunt@icloud.com"
password = "M!CH@e104"

#Switch back to window 1 and enter username
driver.switch_to.window(driver.window_handles[0])
driver.get("https://icloud.com/")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"aid-auth-widget-iFrame")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "account_name_text_field"))).send_keys(username)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sign-in"))).click()

#submitButton = driver.find_element_by_id("sign-in")
#submitButton.click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password_text_field"))).send_keys(password)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sign-in"))).click()

#Exit iframe and click find iphone button
driver.switch_to_default_content()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div/div[2]/div[1]/div"))).click()

#Opens the online Find my page, doesnt give any interactable data?
