from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page



# Create your tests here.
class HomePageTest(TestCase):
    def test_homepage(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>ToDo</title>', html)
        self.assertTrue(html.endswith('</html>'))
