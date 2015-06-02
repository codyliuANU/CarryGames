from django.conf.urls import patterns, url, include
from rest_framework import routers
from authentication import views
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^authcode/$', views.ObtainAuthToken.as_view())
)