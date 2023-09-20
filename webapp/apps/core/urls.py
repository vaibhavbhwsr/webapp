from django.urls import path
from .views import BasePage

app_name = 'core'

urlpatterns = [
    path("", BasePage.as_view(), name="base_page"),
]
