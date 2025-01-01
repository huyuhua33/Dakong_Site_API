"""
URL configuration for DakongSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# URL Configuration (urls.py)
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

# add appliaction
urlpatterns += [
    path('api/website/', include('WebSite.urls')),
    path('api/account/', include('Accounts.urls')),
    path('api/news/', include('News.urls')),
    path('api/products/', include('Products.urls')),
    path('api/media/', include('Media.urls')),
]

from django.conf.urls.static import static
# 開發環境下服務媒體檔案
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# # Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]

# if(settings.DEBUG):
#     # Use static() to add url mapping to serve static files during development (only)
    
#     from django.conf.urls.static import static
#     urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    from drf_yasg.views import get_schema_view

# TODO edit
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="WebSite API",
        default_version="v1",
        description="API documentation for WebSite application",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# JWT setting 
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 獲取訪問和刷新令牌
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新令牌
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # 驗證令牌
    path('api/accounts/', include('Accounts.urls')),  # 用戶管理相關路由
]
