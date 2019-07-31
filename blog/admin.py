from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post,Tags,Comment,CustomUser,Items,Blog
from .forms import (CustomUserCreationForm, CustomUserChangeForm)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tags)
admin.site.register(Items)
admin.site.register(Blog)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
     
    # add page
    add_form = CustomUserCreationForm
    add_fieldsets = (
        ('ID & PASSWORD', {'fields': ('username', 'password1', 'password2')}),
        ('NAME', {'fields': ('first_name', 'last_name','name')}),
        ('PERSONAL INFO', {'fields': ('gender', 'job')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
     
    # change page
    form = CustomUserChangeForm
    fieldsets = (
        ('ID & PASSWORD', {'fields': ('username', 'password')}),
        ('NAME', {'fields': ('first_name', 'last_name','name')}),
        ('PERSONAL INFO', {'fields': ('gender', 'job')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
     
    # list page
    list_display = ['username','name', 'email', 'gender', 'job']
 
 
admin.site.register(CustomUser, CustomUserAdmin)
