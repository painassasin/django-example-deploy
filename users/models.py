from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models

from users.user_manager import EmailUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    objects = EmailUserManager['User']()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: ClassVar[list[str]] = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(email={self.email})'
