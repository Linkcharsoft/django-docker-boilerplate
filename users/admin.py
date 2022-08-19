from django.contrib import admin
from users.models import User_profile


@admin.register(User_profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birthdate']

