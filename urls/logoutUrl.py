from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^logout', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
