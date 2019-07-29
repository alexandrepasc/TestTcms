from django.conf.urls import url

from views import caseViews

urlpatterns = [
    url(r'^case', caseViews.case, name='case'),
    url(r'^case/$', caseViews.case, name='case'),
]
