from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'afrinovate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'afrinovate.views.index', name='index'),

    #url(r'', include('web.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
