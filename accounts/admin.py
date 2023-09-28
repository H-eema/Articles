from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "email",
        "username",
        "city",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("city",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("city",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
