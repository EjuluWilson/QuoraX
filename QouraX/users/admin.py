from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#import the model
from users.models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    #incase of customised model, add form here

    #override
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin) 