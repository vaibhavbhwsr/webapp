from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class MentorProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    mentorship_fee = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.get_full_name()


class MentorshipSession(models.Model):
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return self.title


class MentorshipBooking(models.Model):
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(MentorshipSession, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mentee.username}'s booking of {self.session.title}"
