"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from imggallery.views import GalleryView
# from rest_framework import routers
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from drf_yasg import openapi
from accounts.views import FacebookLogin,GithubLogin


# router = routers.DefaultRouter()
# router.register('images',GalleryView,basename='image')
schema_view = get_schema_view(
    openapi.Info(
        title="Kumarans API",
        default_version='v1',
        description="Welcome to the world of kums APIS",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
app_name = 'review'
urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  
    path('admin/', admin.site.urls),
    path('',include('blog.urls',namespace='blog')),
    path('api/',include('blog_api.urls',namespace='blog_api')),
    path('',include('api.urls',namespace='api')),
    path('',include(('imggallery.urls','images'),namespace='image')),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # all auth dj rest auth
     path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
     path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/github/', GithubLogin.as_view(), name='github_login'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)