from django.contrib import admin
from core import models 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    
admin.site.register(models.User, UserAdmin)