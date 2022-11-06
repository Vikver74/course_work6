
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя
    admin = 'admin'
    user = 'user'


# TODO переопределение пользователя.
# TODO подробности также можно поискать в рекоммендациях к проекту

class User(AbstractBaseUser):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.user)
    image = models.ImageField(null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.admin

    @property
    def is_user(self):
        return self.role == UserRoles.user

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
