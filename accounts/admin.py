from django.contrib import admin
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from .models import CustomUser


class CustomUserAdmin(admin.UserAdmin):
    model = CustomUser
    list_display = [
        'username', 'email', 'last_name', 'first_name',
        'role', 'team', 'is_staff'
    ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = admin.UserAdmin.add_fieldsets + (
        ('None', {'fields': ('role', 'team')}),
    )
    fieldsets = admin.UserAdmin.fieldsets + (
        ('None', {'fields': ('role', 'team')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
