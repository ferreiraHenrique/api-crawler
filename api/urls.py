from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<url>[a-z0-9.]+)/(?P<palavra>[a-z0-9]+)/$', views.run_crawler, name="run_crawler")
]