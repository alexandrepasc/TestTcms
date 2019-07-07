from django.conf.urls import url
from mgrtests import views

urlpatterns = [
    url(r'^product$', views.product, name='product'),
    url(r'^product/$', views.product, name='product'),
]
