from tastypie.resources import ModelResource
from tastypie.api import Api
from models import ExampleData


class ExampleDataResource(ModelResource):

    class Meta:
        queryset = ExampleData.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = []


api = Api(api_name="v1")
api.register(ExampleDataResource())
