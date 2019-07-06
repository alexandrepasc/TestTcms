from django.conf.urls import url
from mgrtests import views

urlpatterns = [
    url(r'^TestMgr$', views.test_mgr, name='testMgr'),
    url(r'^TestMgr/$', views.test_mgr, name='testMgr'),
]
