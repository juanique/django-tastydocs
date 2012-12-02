from django.conf.urls.defaults import patterns
from views import doc

urlpatterns = patterns(
    '',
    (r'^api/$', doc),
    (r'^example/(?P<resource_name>.+)/', 'tastydocs.views.example_data'),
)
