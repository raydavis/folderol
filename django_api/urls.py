from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

from cc_app.api import *
user_resource = UserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_api.views.home', name='home'),
    # url(r'^django_api/', include('django_api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Mostly static
    (r'^$', TemplateView.as_view(template_name="index.html")),

    # API
    (r'^api/', include(user_resource.urls)),
)
