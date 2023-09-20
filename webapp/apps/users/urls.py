from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .views import HomePage, UpdateProfileView

app_name = "users"

urlpatterns = [
    path("home/", HomePage.as_view(), name="home"),
    path("update-profile/", UpdateProfileView.as_view(), name="update_profile"),
    # Password change
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/pass_2/password_change_form.html",
            success_url=reverse_lazy("users:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/pass_2/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
