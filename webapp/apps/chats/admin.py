from django.contrib import admin

from .models import (
    GroupChat,
    Group,
    PrivateChat,
    OneOneGroup,
    VideoChatRoomMember,
    VideoChatMeetRecord,
)

# Register your models here.


admin.site.register(GroupChat)
admin.site.register(Group)
admin.site.register(PrivateChat)
admin.site.register(OneOneGroup)
admin.site.register(VideoChatRoomMember)
admin.site.register(VideoChatMeetRecord)
