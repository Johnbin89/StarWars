"""
URL configuration for starwarspeople project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from people.views import StarWarsCharacterViewSet

router = routers.DefaultRouter()
router.register(r'people', StarWarsCharacterViewSet, basename='people')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls'), name="authentication"),
    path('api/', include(router.urls)),
    path("api-auth/logout/", LogoutView.as_view(), name="logout"),
    path('api-auth/', include('rest_framework.urls')),
    
    #A small bad practice for the live demo deployment :)
    re_path(r'^images/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

#this works only in DEBUG=True anyway
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)