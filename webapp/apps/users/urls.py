from django.urls import path
from .views import HomePage

app_name = "users"

urlpatterns = [
    path("home", HomePage.as_view(), name="home"),
]
