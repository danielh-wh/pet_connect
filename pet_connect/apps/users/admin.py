# django packages
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# local packages
from pet_connect.apps.users.models import User


admin.site.register(User, UserAdmin)
