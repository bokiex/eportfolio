from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from blog.models import Category, Post
from django.test import TestCase

driver = webdriver.Chrome()
driver.maximize_window()
timeout = 10

class TestBlog(TestCase):
    def create_blog(self, title):
        category = Category.objects.get(name="Django")
        b = Post(title = title, body='testtest', category = category)
        b.save()
        return b

    def test_create_blog(self):
        blog = self.create_blog("asdfsadf")
        self.assertIsInstance(blog, Post)
        self.assertEqual(blog.__str__(), "asdfsadf")