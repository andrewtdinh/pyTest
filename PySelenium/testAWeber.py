import unittest
from selenium import webdriver

class AweberTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get('https://www.aweber.com')
        self.assertEqual(self.driver.title,
            'Email Marketing Software from AWeber | AWeber Email Marketing')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
