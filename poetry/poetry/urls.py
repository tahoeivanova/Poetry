
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers, serializers, viewsets
from poems.api_views import TagViewSet, EmelyanovaPoemViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('emelyanova', EmelyanovaPoemViewSet)








from users.models import CustomAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('poems/', include('poems.urls')),
    path('users/', include('users.urls')),
    path('analytics/', include('analytics.urls')),
    path('', views.home_page, name = 'home'),
    path('api/v0/', include(router.urls)),
    path('api_token/', CustomAuthToken.as_view())


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
'''

# from rest_framework.authtoken import views
#
# urlpatterns += [
#     path('api_token/', views.obtain_auth_token)
# ]
