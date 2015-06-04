from django.conf.urls import patterns, include, url
from django.contrib import admin
from authentication import views
from backend import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authentication.urls')),
    url(r'^api-v1/', include('tournament.urls')),
    url(r'^api-v1/log/', include('TLogger.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/auth/authcode/', views.ObtainAuthToken.as_view()),
    url(r'^api/auth/', include('djoser.urls')),
    # MEDIA PATH
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^$', 'backend.views.home', name='home'),
    url(r'^.*$', 'backend.views.home', name='home'),
) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
