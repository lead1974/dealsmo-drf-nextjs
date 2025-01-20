from django.contrib import admin
from django.conf import settings
from django.urls import path


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# Customize admin titles
admin.site.site_header = "DealsMo Admin"
admin.site.site_title = "DealsMo Admin Portal"
admin.site.index_title = "Welcome to DealsMo Admin Portal"