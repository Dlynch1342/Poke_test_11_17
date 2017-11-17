from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home$', views.home, name='home'),
	url(r'^poke/(?P<id>\d+)$', views.poke, name='poke'),
]
	
