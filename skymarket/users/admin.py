from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# from users.models import User, CustomUserAdmin
from users.models import User

# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно

# admin.site.register(User, UserAdmin)
admin.site.register(User)
admin.site.unregister(Group)