from django.conf.urls import url

from views import caseViews

urlpatterns = [
    url(r'^case', caseViews.case, name='case'),
    url(r'^case/$', caseViews.case, name='case'),
    url(r'^newCase', caseViews.new_case, name='newCase'),
    url(r'^newCase/$', caseViews.new_case, name='newCase'),
    url(r'^detailCase/(?P<pk>[0-9a-f-]+)$', caseViews.detail_case, name='detailCase'),
    url(r'^detailCase/(?P<pk>[0-9a-f-]+)/$', caseViews.detail_case, name='detailCase'),
    url(r'^ajax/getSuites/$', caseViews.get_suites, name='getSuites'),
]
