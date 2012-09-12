from django.shortcuts import render_to_response
from django.db import connection
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf import settings

from chocolate.rest import TastyFactory
from tastypie.serializers import Serializer

try:
    from south.management.commands import patch_for_test_db_setup
except ImportError:
    pass


class test_db(object):

    def __init__(self, verbosity=1):
        self.old_db_config = dict(settings.DATABASES["default"])
        self.verbosity = verbosity

    def __enter__(self):
        try:
            patch_for_test_db_setup()
        except NameError:
            pass

        connection.creation.create_test_db(self.verbosity)

    def __exit__(self, type, value, traceback):
        connection.creation.destroy_test_db(self.old_db_config['NAME'], self.verbosity)
        settings.DATABASES['default'] = dict(self.old_db_config)


def doc(request, api):
    api_name = api.api_name

    view_data = {
        'api_url': reverse('api_%s_top_level' % api_name, args=[api_name]),
        'example_url': reverse(
            "tastydocs.views.example_data",
            kwargs={'resource_name': "__RESOURCE_NAME__"}
        )
    }
    return render_to_response(
        'tastydocs/doc.html', view_data,
        context_instance=RequestContext(request))


def example_data(request, resource_name, api):

    tastyfactory = TastyFactory(api)
    resource_mockup = tastyfactory[resource_name]

    with test_db(verbosity=0):
        post_data = resource_mockup.create_post_data()
        get_data = resource_mockup.create_get_data()

    serializer = Serializer()
    json_string = serializer.to_json({
        'POST': post_data,
        'GET': get_data
    })

    return HttpResponse(json_string, mimetype="application/json; charset=utf-8")
