from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions



schema_view = get_schema_view(
    openapi.Info(
        title="DealsMo.com API",
        default_version="v1",
        description="DealsMo.com Management API for Real Estate",
        contact=openapi.Contact(email="email2balda1@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("core_apps.users.urls")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/issues/", include("core_apps.issues.urls")),
    path("api/v1/reports/", include("core_apps.reports.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
]

admin.site.site_header = "DealsMo.com Admin"
admin.site.site_title = "DealsMo.com Admin Portal"
admin.site.index_title = "Welcome to DealsMo.com Admin Portal"