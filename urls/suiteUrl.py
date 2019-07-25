from django.conf.urls import url

from views import suiteViews

urlpatterns = [
    url(r'^suite$', suiteViews.suite, name='suite'),
    url(r'^suite/$', suiteViews.suite, name='suite'),
    url(r'^newSuite$', suiteViews.new_suite, name='newSuite'),
    url(r'^newSuite/$', suiteViews.new_suite, name='newSuite'),
    url(r'^detailSuite/(?P<pk>[0-9a-f-]+)$', suiteViews.detail_suite, name='detailSuite'),
    url(r'^detailSuite/(?P<pk>[0-9a-f-]+)/$', suiteViews.detail_suite, name='detailSuite'),
]
