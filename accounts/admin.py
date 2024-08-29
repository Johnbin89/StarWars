from django.contrib import admin
from accounts.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    filter_horizontal = ("favorites", )
    
    
admin.site.register(User, UserAdmin)