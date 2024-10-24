from django.contrib import admin
from .models import User, Profile
# Register your models here.


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = (
        'id','username', 'email', 
        'first_name', 'last_name', 
        'is_staff', 'is_active')
    

@admin.register(Profile)
class ProfileUser(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'first_name', 'last_name',
        'birth_date', 'profile_image', 'status',
        'phone', 'country'
    )