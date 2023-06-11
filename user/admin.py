from django.contrib import admin
from .models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

user = get_user_model()


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'username', 'email', 'password', 'first_name',
         'last_name', 'gender', 'height', 'date_of_birth', 'age', 'profile_pic')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        })
    )
    model = user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'id', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username','email', 'first_name', 'last_name')
    ordering = ('id')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(user, UserAdmin)
