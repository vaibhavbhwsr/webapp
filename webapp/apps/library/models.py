from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel

# Create your models here.


class Book(BaseModel):
    CONDITION = (
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publication_year = models.PositiveIntegerField()
    condition = models.CharField(max_length=20, choices=CONDITION)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_available_for_borrow = models.BooleanField(default=False)
    is_available_for_sale = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to="book_covers/", blank=True, null=True)

    def __str__(self):
        return self.title
