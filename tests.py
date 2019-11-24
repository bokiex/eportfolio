from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from blog.models import Category, Post
from django.db import models
from django.test import TestCase
driver = webdriver.Chrome()
driver.maximize_window()
timeout = 10


# Log In
def test_unsuccessful_login():
    driver.get("http://127.0.0.1:8000/admin/")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//input[@value='Log in']")
    name.send_keys("wrongusername")
    password.send_keys("wrongpassword")
    submit.click()
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "errornote"))
    assert(element_present)

def test_login():
    nameString = "bokie"
    passString="123123"
    driver.get("http://127.0.0.1:8000/admin/")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//input[@value='Log in']")
    name.send_keys(nameString)
    password.send_keys(passString)
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//h1[text()='Site administration']"))
    assert(element_present)

# Add User
def test_bad_name_add_user():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/auth/user/add/')]")
    add.click()
    element_present = EC.presence_of_element_located((By.ID, "id_username"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password1")
    password2 = driver.find_element_by_name("password2")
    submit = driver.find_element_by_name("_addanother")
    name.send_keys("!@#$%^&*()")
    password.send_keys("123123123D")
    password2.send_keys("123123123D")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//li[text()='Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.']"))
    assert(element_present)

def test_bad_password_add_user():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/auth/user/add/')]")
    add.click()
    element_present = EC.presence_of_element_located((By.ID, "id_username"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password1")
    password2 = driver.find_element_by_name("password2")
    submit = driver.find_element_by_name("_addanother")
    name.send_keys("goodname/10")
    password.send_keys("badpass")
    password2.send_keys("badpass")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//li[text()='This password is too short. It must contain at least 8 characters.']"))
    assert(element_present)

def test_bad_second_pass_add_user():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/auth/user/add/')]")
    add.click()
    element_present = EC.presence_of_element_located((By.ID, "id_username"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password1")
    password2 = driver.find_element_by_name("password2")
    submit = driver.find_element_by_name("_addanother")
    name.send_keys("goodname/10")
    password.send_keys("123123123D")
    password2.send_keys("123123123")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//li[text()='The two password fields didn't match.']"))
    assert(element_present)

def test_successful_add_user():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/auth/user/add/')]")
    add.click()
    element_present = EC.presence_of_element_located((By.ID, "id_username"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password1")
    password2 = driver.find_element_by_name("password2")
    submit = driver.find_element_by_name("_addanother")
    name.send_keys("goodname/10")
    password.send_keys("123123123D")
    password2.send_keys("123123123D")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//li[@class='success']"))
    assert(element_present)


# Add Blog
def test_add_successful_blog():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/blog/post/add/')]")
    add.click()

    element_present = EC.presence_of_element_located((By.ID, "id_title"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    
    title = driver.find_element_by_name("title")
    body = driver.find_element_by_name("body")
    category = driver.find_element_by_xpath("//select[@id='id_categories']/option[text()='Django']")
    save = driver.find_element_by_name("_save")
    title.send_keys("This is a test blog")
    body.send_keys("This is a test body")

    category.click()    
    save.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//li[@class='success']"))
    assert(element_present)
    
def test_bad_title_blog():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/blog/post/add/')]")
    add.click()

    element_present = EC.presence_of_element_located((By.ID, "id_title"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    
    body = driver.find_element_by_name("body")
    category = driver.find_element_by_xpath("//select[@id='id_categories']/option[text()='Django']")
    save = driver.find_element_by_name("_save")
    body.send_keys("This is a test body")

    category.click()    
    save.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//p[text()='Please correct the errors below.']"))
    assert(element_present)

def test_add_bad_title_blog():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/blog/post/add/')]")
    add.click()

    element_present = EC.presence_of_element_located((By.ID, "id_title"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)

    body = driver.find_element_by_name("body")
    category = driver.find_element_by_xpath("//select[@id='id_categories']/option[text()='Django']")
    save = driver.find_element_by_name("_save")
    body.send_keys("This is a test body")

    category.click()    
    save.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//p[text()='Please correct the errors below.']"))
    assert(element_present)

# Category
def test_add_category():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/blog/category/add/')]")
    add.click()

    element_present = EC.presence_of_element_located((By.ID, "id_name"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)

    name = driver.find_element_by_name("name")
    save = driver.find_element_by_name("_save")
    name.send_keys("Test Category")

    save.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//li[@class='success']"))
    assert(element_present)

def test_bad_name_add_category():
    driver.get("http://127.0.0.1:8000/admin/")
    add = driver.find_element_by_xpath("//a[contains(@href,'/admin/blog/category/add/')]")
    add.click()

    element_present = EC.presence_of_element_located((By.ID, "id_name"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)

    save = driver.find_element_by_name("_save")

    save.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//div[@class='field-name']/ul/li[text()='This field is required.']"))
    assert(element_present)
        
# Log out
def test_logout():
    logout = driver.find_element_by_xpath("//a[contains(@href,'/admin/logout/')]")
    logout.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//h1[text()='Logged out']"))
    WebDriverWait(driver, timeout).until(element_present)

# Project
def test_project_connection():
    driver.get("http://127.0.0.1:8000/projects/")
    element_present = EC.presence_of_element_located((By.ID, "portfolioBody"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)

def test_navigate_to_project():
    driver.get("http://127.0.0.1:8000/blog/")
    home_button = driver.find_element_by_xpath("//a[text()='Home']")
    home_button.click()
    element_present = EC.presence_of_element_located((By.ID, "portfolioBody"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)

def test_view_project_detail():
    driver.get("http://127.0.0.1:8000/projects/")
    python = driver.find_element_by_xpath("//a[@href='/projects/6/']")
    python.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//p[text()='A python test script']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

# Blog
def test_blog_connection():
    driver.get("http://127.0.0.1:8000/blog/")
    element_present = EC.presence_of_element_located((By.ID, "portfolioBody"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)

def test_view_blog_detail():
    driver.get("http://127.0.0.1:8000/blog/")
    blogpost = driver.find_element_by_xpath("//a[@href='/blog/1/']")
    blogpost.click()
    element_present = EC.presence_of_element_located((By.XPATH, "//input[@name='author']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

# Add comment
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
    element_present = EC.presence_of_element_located((By.XPATH,"//div[@class='commentBody']/p[text()='TestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTestTest']"))
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

def test_unique_char_name():
    string = "MY%nameis!@#$%^&*()"
    driver.get("http://127.0.0.1:8000/blog/1/")
    author = driver.find_element_by_name("author")
    body = driver.find_element_by_name("body")
    submit = driver.find_element_by_xpath("//button[text()='Submit']")
    author.send_keys(string)
    body.send_keys("Test Comment")
    submit.click()
    element_present = EC.presence_of_element_located((By.XPATH,"//div[@class='commentAuthor']/p/b[text()='MY%nameis!@#$%^&*()']"))
    wait = WebDriverWait(driver,timeout).until(element_present)
    assert(wait)
    driver.back()

