from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^groundup/', include('groundup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name="about"),
    url(r'^contact/$', 'flatpage', {'url': '/contact/'}, name="contact"),
    url(r'^facts/$', 'flatpage', {'url': '/facts/'}, name="facts"),
    url(r'^$', 'flatpage', {'url': '/'}, name='home'),

)

urlpatterns += patterns('',
	url(r'^blog/', include('blog.urls')),
)

urlpatterns += staticfiles_urlpatterns()
