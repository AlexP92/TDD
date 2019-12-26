from selenium import webdriver
import unittest

class VisitorTest(unittest.TestCase):

    def setUp(self):
       self.browser = webdriver.Chrome()

    def tearDown(self):
       self.browser.close()


    def test_starting(self):

        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn( "ToDo",self.browser.title)

        print("succes")

if __name__=="__main__":
    unittest.main(warnings='ignore')



