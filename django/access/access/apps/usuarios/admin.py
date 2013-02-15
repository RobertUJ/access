from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin

from access.apps.usuarios.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Informacion de perfil'

# # Define a new User admin
class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
