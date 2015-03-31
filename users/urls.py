from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
        url(r'^(?P<user_id>\d+)/edit/$', views.edit, name='edit'),
)
