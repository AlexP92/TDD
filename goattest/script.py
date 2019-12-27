from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class VisitorTest(unittest.TestCase):

    def setUp(self):
       self.browser = webdriver.Chrome()
       self.browser.implicitly_wait(3)

    def tearDown(self):
       self.browser.close()


    def test_starting(self):

        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn( "ToDo",self.browser.title)
        header=self.browser.find_element_by_tag_name('h1')
        self.assertIn("To Do",header.text)
        inputbox =self.browser.find_element_by_id("add_new_item")
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to do item')
        inputbox.send_keys("Buy peacock")
        inputbox.send_keys(Keys.ENTER)

        table=self.browser.find_element_by_id('list_table')
        rows=table.find_elements_by_tag_name('tr')

        self.assertTrue(
            any(row.text == '1: Buy peacock' for row in rows),
            "New to-do item did not appear in table"
        )
        # inputbox = self.browser.find_element_by_id("add_new_item")
        # inputbox.send_keys("Fly peacock")
        # inputbox.send_keys(Keys.ENTER)
        # self.assertIn("1: Buy peacock", [row.text for row in rows])
        self.fail('finish')

if __name__=="__main__":
    unittest.main(warnings='ignore')



