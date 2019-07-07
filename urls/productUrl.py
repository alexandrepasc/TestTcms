from django.conf.urls import url
from mgrtests import views

urlpatterns = [
    url(r'^Product$', views.test_mgr, name='Product'),
    url(r'^Product/$', views.test_mgr, name='Product'),
]
