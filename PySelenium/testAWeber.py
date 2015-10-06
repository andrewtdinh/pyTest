import unittest
from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class AweberTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox()
        cls.driver = webdriver.Chrome()

    def test_title(self):
        self.driver.get('https://www.aweber.com')
        self.assertEqual(self.driver.title,
            'Email Marketing Software from AWeber | AWeber Email Marketing')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
