from django.conf.urls import url
from views import productViews

urlpatterns = [
    url(r'^product$', productViews.product, name='product'),
    url(r'^product/$', productViews.product, name='product'),
    url(r'^newProduct/$', productViews.new_product, name='newProduct'),
    url(r'^newProduct/?(\S)$', productViews.new_product, name='newProduct'),
    url(r'^detailProduct/(?P<pk>[0-9a-f-]+)$', productViews.detail_product, name='detailProduct'),
    url(r'^detailProduct/(?P<pk>[0-9a-f-]+)/?(\S)$', productViews.detail_product, name='detailProduct'),
    url(r'^editProduct/(?P<pk>[0-9a-f-]+)$', productViews.edit_product, name='editProduct'),
]
