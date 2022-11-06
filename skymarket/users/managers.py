from django.contrib.auth.models import (
    BaseUserManager
)
# TODO здесь должен быть менеджер для модели Юзера.
# TODO Поищите эту информацию в рекомендациях к проекту


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, role='user', password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone=phone
        )

        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, role='admin', password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone=phone
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

        return user
