from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication API",
        default_version='v1',
        description="API for user authentication for DocuConta",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@docuConta.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_app.urls'), name='auth_app'),
    path('api/profile/', include('profile_app.urls'), name='profile_app'),
    path('api/task/', include('task_app.urls'), name='task_app'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
