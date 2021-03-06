from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^auth/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^auth/login/$', 'django.contrib.auth.views.login'),
    url(r'^media/(.*)','django.views.static.serve',{'document_root':MEDIA_ROOT}),
    url(r'^$', 'b13.views.index', name='index'),
    url(r'^home/$', 'b13.views.home', name='home'),
    url(r'^faleconosco/$', 'b13.views.faleconosco', name='faleconosco'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^news/', include('b13.news.urls')),
    url(r'^albuns/', include('b13.albuns.urls')),
    url(r'^videos/', include('b13.videos.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
