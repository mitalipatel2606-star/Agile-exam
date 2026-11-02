from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///Users/mitalipatel/Downloads/Agile%20exam/login.html")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)
assert "Login Successful" in driver.page_source

driver.get("file:///Users/mitalipatel/Downloads/Agile%20exam/login.html")

driver.find_element(By.ID, "username").send_keys("wrong")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)
assert "Invalid credentials" in driver.page_source

print("Both tests passed!")
driver.quit()