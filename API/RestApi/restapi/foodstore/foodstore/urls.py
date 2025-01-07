"""foodstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
# from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt import authentication
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets APj",
      default_version='v1',
      description="it will perform crud operation",
      terms_of_service="http://127.0.0.1:8000/",
      contact=openapi.Contact(email="vasanth@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(authentication.JWTAuthentication,),
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',swagger_auto_schema(methods=['post'],security=[])(TokenObtainPairView.as_view())),
    path('api/token/refresh/',swagger_auto_schema(methods=['post'],security=[])(TokenRefreshView.as_view())),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/chef',include('Chef.urls')),
    path('api/dish',include('Dish.urls')),
    # path('api/user/', include('user.urls')),
]

