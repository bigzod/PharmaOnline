from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views

urlpatterns = patterns('',
    url(r'^$', 'website.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', include('haystack.urls')),
)
