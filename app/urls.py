"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from shared_resources.common.swagger.swagger import get_swagger_config

router = DefaultRouter()
schema_view = get_swagger_config()
urlpatterns = [
    path("admin/", admin.site.urls),

    path('swagger.json', schema_view.without_ui(cache_timeout=10), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=10), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='access_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    
    path('api/', include('src.item.urls')),
    path('api/', include('src.category.urls')),
]
