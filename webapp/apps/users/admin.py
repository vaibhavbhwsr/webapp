from django.contrib import admin

from .models import (
    MentorProfile,
    MentorshipBooking,
    MentorshipSession,
    Skill,
    UserSkill,
    SkillProgress,
)

# Register your models here.

admin.site.register(MentorProfile)
admin.site.register(MentorshipBooking)
admin.site.register(MentorshipSession)

admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(SkillProgress)
