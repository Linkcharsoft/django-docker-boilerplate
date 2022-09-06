from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from users.models import User_profile

admin.site.register(User, UserAdmin)

@admin.register(User_profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthdate']

