from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client


class BaseTestCase(TestCase):

    def assertInstanceOf(self, class_obj, instance):
        self.assertTrue(isinstance(instance, class_obj))

    def assertNotEmpty(self, value):
        self.assertTrue(value != [] and value != "")


class DocsTestCase(BaseTestCase):

    def get_example_url(self, resource_name):
        kwargs = {
            'resource_name': resource_name,
        }

        return reverse("tastydocs.views.example_data", kwargs=kwargs)

    def test_example_data(self):
        "Example data can be requested using a json webservice"

        client = Client()

        url = self.get_example_url("comment")
        response = client.get(url)
        content_type = response._headers['content-type'][1]

        self.assertEquals(200, response.status_code)
        self.assertTrue(content_type.startswith("application/json"))
        self.assertTrue("/api/v1/post/1/" in response.content, response.content)

    def test_docs_twise(self):
        "BUG REPRO: Cannot request example data twice."

        client = Client()

        url = self.get_example_url("comment")
        response = client.get(url)
        response = client.get(url)  # yes, twice

        self.assertEquals(200, response.status_code)
