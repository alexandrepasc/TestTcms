from django.conf.urls import url
from views import versionViews

urlpatterns = [
    url(r'^version', versionViews.version, name='version'),
    url(r'^version/$', versionViews.version, name='version'),
    url(r'^newVersion/$', versionViews.new_version, name='newVersion'),
    url(r'^newVersion/?(\S)$', versionViews.new_version, name='newVersion'),
    url(r'^detailVersion/(?P<pk>[0-9a-f-]+)$', versionViews.detail_version, name='detailVersion'),
    url(r'^detailVersion/(?P<pk>[0-9a-f-]+)/?(\S)$', versionViews.detail_version, name='detailVersion'),
]
