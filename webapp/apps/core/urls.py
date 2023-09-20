from django.contrib.auth import views as auth_views
from django.urls import path

from .views import IndexView, MyLoginView, MySignupView

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("signup/", MySignupView.as_view(), name="signup"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]
