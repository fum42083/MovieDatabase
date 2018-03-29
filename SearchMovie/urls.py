from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^list/$', views.list, name='list'),
	url(r'^show/$', views.show, name='show'),
	url(r'^analyze/$', views.analyze, name='analyze')
]