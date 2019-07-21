from django.conf.urls import url

from views import suiteViews

urlpatterns = [
    url(r'^suite$', suiteViews.suite, name='suite'),
    url(r'^suite/$', suiteViews.suite, name='suite'),
]
