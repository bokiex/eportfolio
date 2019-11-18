from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
timeout = 5

def test_login():
    driver.get("http://127.0.0.1:8000/admin/")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//input[@value='Log in']")
    name.send_keys("wrongusername")
    password.send_keys("wrongpassword")
    submit.click()

def test_connection():
    driver.get("http://127.0.0.1:8000/projects/")
    element_present = EC.presence_of_element_located((By.ID, "portfolioBody"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
