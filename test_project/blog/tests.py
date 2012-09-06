from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
import json


class BaseTestCase(TestCase):

    def assertInstanceOf(self, class_obj, instance):
        self.assertTrue(isinstance(instance, class_obj))

    def assertNotEmpty(self, value):
        self.assertTrue(value != [] and value != "")


class DocsTestCase(BaseTestCase):

    def test_example_data(self):
        "Example data can be requested using a json webservice"

        client = Client()
        kwargs = {
            'resource_name': 'comment',
        }

        url = reverse("tastydocs.views.example_data", kwargs=kwargs)

        response = client.get(url)
        content_type = response._headers['content-type'][1]

        self.assertEquals(200, response.status_code)
        self.assertTrue(content_type.startswith("application/json"))
        self.assertTrue("/api/v1/post/1/" in response.content, response.content)
