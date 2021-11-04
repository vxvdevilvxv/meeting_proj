from django.contrib import admin
from .models import *


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'avatar', 'email')


class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender')


admin.site.register(Person, PersonAdmin)
admin.site.register(Gender, GenderAdmin)
