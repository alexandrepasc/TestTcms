from django.conf.urls import url

from views import tagViews

urlpatterns = [
    url(r'^tag', tagViews.tag, name='tag'),
    url(r'^tag/$', tagViews.tag, name='tag'),
    url(r'^tag/?(\S)$', tagViews.tag, name='tag'),
    url(r'^newTag/$', tagViews.new_tag, name='newTag'),
    url(r'^newTag/?(\S)$', tagViews.new_tag, name='newTag'),
    url(r'^detailTag/(?P<pk>[0-9a-f-]+)$', tagViews.detail_tag, name='detailTag'),
    url(r'^detailTag/(?P<pk>[0-9a-f-]+)/?(\S)$', tagViews.detail_tag, name='detailTag'),
    url(r'^editTag/(?P<pk>[0-9a-f-]+)$', tagViews.edit_tag, name='editTag'),
]
