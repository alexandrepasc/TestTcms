from django.conf.urls import url

from views import componentViews

urlpatterns = [
    url(r'^component$', componentViews.component, name='component'),
    url(r'^component/$', componentViews.component, name='component'),
    url(r'^component/?(\S)$', componentViews.component, name='component'),
    url(r'^newComponent/$', componentViews.new_component, name='newComponent'),
    url(r'^newComponent/?(\S)$', componentViews.new_component, name='newComponent'),
    url(r'^detailComponent/?(\S)$', componentViews.detail_component, name='detailComponent'),
    url(r'^detailComponent/(?P<pk>[0-9a-f-]+)$', componentViews.detail_component, name='detailComponent'),
    url(r'^detailComponent/(?P<pk>[0-9a-f-]+)/?(\S)$', componentViews.detail_component, name='detailComponent'),
    url(r'^editComponent/(?P<pk>[0-9a-f-]+)$', componentViews.edit_component, name='editComponent'),
    url(r'^deleteComponent/(?P<pk>[0-9a-f-]+)$', componentViews.delete_component, name='deleteComponent'),
]
