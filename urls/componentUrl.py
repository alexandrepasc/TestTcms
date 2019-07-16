from django.conf.urls import url

from views import componentViews

urlpatterns = [
    url(r'^component$', componentViews.component, name='component'),
    url(r'^component/$', componentViews.component, name='component'),
    url(r'^component/?(\S)$', componentViews.component, name='component'),
    url(r'^newComponent/$', componentViews.new_component, name='newComponent'),
    url(r'^newComponent/?(\S)$', componentViews.new_component, name='newComponent'),
]
