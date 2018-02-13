from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reporter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('Apis.urls')),

)

# urlpatterns += patterns('', (
#     r'^static/(?P<path>.*)$',
#     'django.views.static.serve',
#     {'document_root': settings.STATIC_ROOT}
# ))

# urlpatterns += patterns('', (
#     r'^media/(?P<path>.*)$',
#     'django.views.static.serve',
#     {'document_root': settings.MEDIA_ROOT}
# ))
