from django.contrib import admin
from .models import user

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','username','Email','mobile_no','Address','gender','age']