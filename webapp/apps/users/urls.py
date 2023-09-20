from django.urls import path

from .views import HomePage, UpdateProfileView

app_name = "users"

urlpatterns = [
    path("home/", HomePage.as_view(), name="home"),
    path(
        "update-profile/", UpdateProfileView.as_view(), name="update_profile"
    ),
]
