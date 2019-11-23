from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from blog.models import Category, Post
from django.test import TestCase

# driver = webdriver.Chrome()
# driver.maximize_window()
# timeout = 10

# class TestBlog(TestCase):
#     def create_category(self, name):
#         return Category.objects.create(name=name)

#     def test_category(self):
#         category = self.create_category("Test")
#         self.assertIsInstance(category, Category)
#         self.assertEqual(category.__str__(), "Test")
