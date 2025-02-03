from django.urls import path, re_path, include

from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    LogoutAPIView,
    UserCreateView,
    TokenView,
    MeView,
)

app_name = 'user'

urlpatterns = [
    re_path(
        r"^o/(?P<provider>\S+)/$",
        CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
    path("create/", UserCreateView.as_view(), name="create"),
    path("token/", TokenView.as_view(), name="token"),
    path("me/", MeView.as_view(), name="me"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]