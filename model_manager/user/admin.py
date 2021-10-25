from django.contrib import admin
from .models import users,Detail

@admin.register(users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','username','Email','mobile_no','Address','gender','age']

@admin.register(Detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','username','age']