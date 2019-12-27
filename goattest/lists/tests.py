from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # def test_homepage_post(self):
    #     request = HttpRequest()
    #     request.method='post'
    #     request.POST['item_text']='A new item'
    #     response = home_page(request)
    #
    #     self.assertIn('A new item',response.content.decode())
