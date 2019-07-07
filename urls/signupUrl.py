from django.conf.urls import url

from accounts import views as accounts_views


urlpatterns = [
    url(r'^signup$', accounts_views.signup, name='signup'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
]
