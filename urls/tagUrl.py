from django.conf.urls import url

from views import tagViews

urlpatterns = [
    url(r'^tag', tagViews.tag, name='tag'),
    url(r'^tag/$', tagViews.tag, name='tag'),
]
