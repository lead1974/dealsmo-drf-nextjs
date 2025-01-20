from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.views.debug import default_urlconf


schema_view = get_schema_view(
    openapi.Info(
        title="DealsMo API",
        default_version="v1",
        description="DealsMoAPI for Real Estate",
        contact=openapi.Contact(email="email2balda1@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", default_urlconf),  # This will show the default Django welcome page
    path(settings.ADMIN_URL, admin.site.urls),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

admin.site.site_header = "DealsMo Admin"
admin.site.site_title = "DealsMo Admin Portal"
admin.site.index_title = "Welcome to DealsMo Admin Portal"