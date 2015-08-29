from django.conf.urls import patterns, include, url
from django.contrib import admin
from esculturas import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^getData$', views.get_data),
)