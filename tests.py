from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def test_connection():
    driver = webdriver.Chrome()
    driver.fullscreen_window()
    driver.get("http://127.0.0.1:8000/projects/")
    timeout = 5
    elem = driver.find_elements_by_id("portfolioBody")

    element_present = EC.presence_of_element_located(elem)
    assert(WebDriverWait(driver, timeout).until(element_present))    

