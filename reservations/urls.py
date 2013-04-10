from django.conf.urls import patterns, include, url

urlpatterns = patterns('reservations.views',
	url(r'^$', 'index'),
)