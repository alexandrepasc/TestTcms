from django.conf.urls import url
from views import versionViews

urlpatterns = [
    url(r'^version', versionViews.version, name='version'),
    url(r'^version/$', versionViews.version, name='version'),
    url(r'^newVersion/$', versionViews.new_version, name='newVersion'),
    url(r'^newVersion/?(\S)$', versionViews.new_version, name='newVersion'),
]
