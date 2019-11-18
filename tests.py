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

def test_navigate_to_project():
    driver.get("http://127.0.0.1:8000/blog/")


def test_view_project_detail():
    driver.get("http://127.0.0.1:8000/projects/")
    python = driver.find_element_by_xpath("//a[@href='/projects/6/']")
    python.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//p[text()='A python test script']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

def test_view_blog_detail():
    driver.get("http://127.0.0.1:8000/blog/")
    blogpost = driver.find_element_by_xpath("//a[@href='/blog/1/']")
    blogpost.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//input[@name='author']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

def test_add_valid_comment():
    driver.get("http://127.0.0.1:8000/blog/1/")
    author = driver.find_element_by_name("author")
    body = driver.find_element_by_name("body")
    submit = driver.find_element_by_xpath("//button[text()='Submit']")
    author.send_keys("Test Name")
    body.send_keys("Test Comment")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH,"//div[@class='commentBody']/p"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

def test_long_string_comment():
    string = "Test"
    count = 0
    driver.get("http://127.0.0.1:8000/blog/1/")
    author = driver.find_element_by_name("author")
    body = driver.find_element_by_name("body")
    submit = driver.find_element_by_xpath("//button[text()='Submit']")

    while (count < 10):
        string = string * 2
        count+= 1
    author.send_keys("Test Name")
    body.send_keys(string)
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH,"//div[@class='commentBody']/p[text()='TestTestTestTestTestTestTestTestTestTestTestTestTestTestTest']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

def test_long_string_name():
    string = "Test"
    count = 0
    driver.get("http://127.0.0.1:8000/blog/1/")
    author = driver.find_element_by_name("author")
    body = driver.find_element_by_name("body")
    submit = driver.find_element_by_xpath("//button[text()='Submit']")
    while (count < 3):
        string = string * 2
        count+= 1
    author.send_keys(string)
    body.send_keys("Test Comment")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH,"//div[@class='commentAuthor']/p/b[text()='TestTestTestTestTest']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()