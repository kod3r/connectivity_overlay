from django.conf.urls import patterns, include, url

from ua.views import index
from tileserver import render_tile

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.http import HttpResponse


def test_return(request, num1, num2, num3):
    return HttpResponse("Input numbers:" + str(num1) + str(num2) + str(num3))

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'tile/(\d+)/(\d+)/(\d+)/$', test_return),


    # Examples:
    # url(r'^$', 'ua.views.home', name='home'),
    # url(r'^ua/', include('ua.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
