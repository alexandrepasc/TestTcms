from django.conf.urls import url
from views import versionViews

urlpatterns = [
    url(r'^version', versionViews.version, name='version'),
    url(r'^version/$', versionViews.version, name='version'),
]
