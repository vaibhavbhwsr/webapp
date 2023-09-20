from django.contrib import admin

from .models import MentorProfile, MentorshipBooking, MentorshipSession

# Register your models here.

admin.site.register(MentorProfile)
admin.site.register(MentorshipBooking)
admin.site.register(MentorshipSession)
