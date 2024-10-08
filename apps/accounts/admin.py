from django.contrib import admin
from .models import User
# Register your models here.


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = (
        'id','username', 'email', 
        'first_name', 'last_name', 
        'is_staff', 'is_active')