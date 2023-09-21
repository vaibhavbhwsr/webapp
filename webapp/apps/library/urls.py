from django.urls import path

from .views import BookView


app_name = "library"

urlpatterns = [
    path("books/", BookView.as_view(), name="books"),
]
