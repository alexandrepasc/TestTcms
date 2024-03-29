from django.conf.urls import url

from views import versionViews

urlpatterns = [
    url(r'^version', versionViews.version, name='version'),
    url(r'^version/$', versionViews.version, name='version'),
    url(r'^version/?(\S)$', versionViews.version, name='version'),
    url(r'^newVersion/$', versionViews.new_version, name='newVersion'),
    url(r'^newVersion/?(\S)$', versionViews.new_version, name='newVersion'),
    url(r'^detailVersion/?(\S)$', versionViews.detail_version, name='detailVersion'),
    url(r'^detailVersion/(?P<pk>[0-9a-f-]+)$', versionViews.detail_version, name='detailVersion'),
    url(r'^detailVersion/(?P<pk>[0-9a-f-]+)/?(\S)$', versionViews.detail_version, name='detailVersion'),
    url(r'^editVersion/(?P<pk>[0-9a-f-]+)$', versionViews.edit_version, name='editVersion'),
    url(r'^deleteVersion/(?P<pk>[0-9a-f-]+)$', versionViews.delete_version, name='deleteVersion'),
]
