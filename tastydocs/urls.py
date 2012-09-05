from django.conf.urls.defaults import patterns, include
from views import doc
from api import api

urlpatterns = patterns(
    '',
    (r'^api$', doc),
    (r'^api', include(api.urls)),
)
