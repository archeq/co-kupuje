from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField


def get_user_directory(instance, filename) -> str:
    return f"users/{instance.username}/{filename}"


class User(AbstractUser):
    """Custom user model extending Django's AbstractUser."""

    # field length constants
    USERNAME_MAX_LENGTH = 32
    USERNAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 32

    # authentication fields
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        blank=False,
        null=False,
        validators=[validators.MinLengthValidator(USERNAME_MIN_LENGTH)],
        primary_key=True,
        editable=False,
    )
    email = models.EmailField(unique=True, blank=False, null=False)

    # profile fields
    profile_picture = models.ImageField(
        upload_to=get_user_directory,
        blank=True,
        null=True,
    )
    real_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        null=True,
        verbose_name='name',
    )
    country = CountryField(blank=True, null=True)

    # metadata fields
    registration_date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-registration_date']

    def __str__(self):
        return self.username