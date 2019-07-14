from django.conf.urls import url

from views import tagViews

urlpatterns = [
    url(r'^tag', tagViews.tag, name='tag'),
    url(r'^tag/$', tagViews.tag, name='tag'),
    url(r'^newTag/$', tagViews.new_tag, name='newTag'),
    url(r'^newTag/?(\S)$', tagViews.new_tag, name='newTag'),
]
