"""poetry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers, serializers, viewsets
from poems.api_views import PoetViewSet, TagViewSet, EmelyanovaPoemViewSet, PoemPushkinViewSet, PoemLermontovViewSet, PoemAkhmadulinaViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('emelyanova', EmelyanovaPoemViewSet)

router_test_drive = routers.DefaultRouter()


router_test_drive.register('poets', PoetViewSet)
router_test_drive.register('pushkin', PoemPushkinViewSet, basename='pushkin')
router_test_drive.register('akhmadulina', PoemAkhmadulinaViewSet, basename='akhmadulina')
router_test_drive.register('lermontov', PoemLermontovViewSet, basename='lermontov')







from users.models import CustomAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('poems/', include('poems.urls')),
    path('users/', include('users.urls')),
    path('analytics/', include('analytics.urls')),
    path('', views.home_page, name = 'home'),
    path('api/v0/', include(router.urls)),
    path('api/test_drive/v0/', include(router_test_drive.urls)),
    path('api_token/', CustomAuthToken.as_view())


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

# from rest_framework.authtoken import views
#
# urlpatterns += [
#     path('api_token/', views.obtain_auth_token)
# ]
