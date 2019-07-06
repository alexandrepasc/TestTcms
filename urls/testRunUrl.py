from django.conf.urls import url
from mgrtests import views

urlpatterns = [
    url(r'^TestRun$', views.test_run, name='testRun'),
    url(r'^TestRun/$', views.test_run, name='testRun'),
]
