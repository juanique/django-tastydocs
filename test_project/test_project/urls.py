from django.conf.urls import patterns, include
from blog.api import api

urlpatterns = patterns(
    '',
    (r'^api/', include(api.urls)),
    (r'^docs/', include("tastydocs.urls"), {"api_name": "v1"}),
)
