from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *
from archivoDigital.forms import UserChangeForm, UserCreationForm


class UserAdmin(auth_admin.UserAdmin):
    list_display = ('first_name','last_name','email','area','is_active')
    fieldsets = (
        ('Credenciales de acceso', {'fields': ('email', 'password')}),
        ('Información del Usuario', {'fields': ('first_name', 'last_name','area','cargo','phone','extension','photo')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Fechas', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Información del Usuario', {'fields': ('first_name', 'last_name','photo')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)} #'password1', 'password2')}
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined','is_superuser',)


admin.site.register(User, UserAdmin)
