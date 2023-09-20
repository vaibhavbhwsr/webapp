from django.urls import path
from .views import IndexView, MyLoginView, SignupPage

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="main_page"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("signup/", SignupPage.as_view(), name="signup"),
]
