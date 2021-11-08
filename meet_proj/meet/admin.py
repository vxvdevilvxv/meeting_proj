from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'user', 'first_name', 'last_name', 'gender', 'avatar', 'email')
    list_display_links = ('id', 'first_name')
    readonly_fields = ('user',)

    def get_photo(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width=75>')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


admin.site.register(UserProfile, UserProfileAdmin)
