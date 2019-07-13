from django.conf.urls import url
from mgrtests import views

urlpatterns = [
    url(r'^product$', views.product, name='product'),
    url(r'^product/$', views.product, name='product'),
    url(r'^newProduct/$', views.new_product, name='newProduct'),
    url(r'^detailProduct/(?P<id>[0-9a-f-]+)$', views.detail_product, name='detailProduct'),
    url(r'^detailProduct/(?P<id>[0-9a-f-]+)/?(\S)$', views.detail_product, name='detailProduct'),
    url(r'^detailEditProduct/(?P<id>[0-9a-f-]+)$', views.detail_edit_product, name='detailEditProduct'),
]
