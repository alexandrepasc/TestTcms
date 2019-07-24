from django.conf.urls import url

from views import suiteViews

urlpatterns = [
    url(r'^suite$', suiteViews.suite, name='suite'),
    url(r'^suite/$', suiteViews.suite, name='suite'),
    url(r'^newSuite$', suiteViews.new_suite, name='newSuite'),
    url(r'^newSuite/$', suiteViews.new_suite, name='newSuite'),
]
