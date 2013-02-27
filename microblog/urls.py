from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", views.HomepageView.as_view(), name="home"),
    url(r'^blog/', include("blog.urls", namespace="blog")),

    url(r'^admin/', include(admin.site.urls)),
)
