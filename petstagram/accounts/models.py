from enum import Enum
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.accounts.validators import only_alpha_validator


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.value) for choice in cls]


class ChoicesStringMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringMixin, Enum):
    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"


class PetstagramUser(AbstractUser):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 30
    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_alpha_validator,
        )
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_alpha_validator,
        )
    )
    email = models.EmailField(unique=True)
    profile_picture = models.URLField(blank=True, null=True)
    gender = models.CharField(
        max_length=Gender.max_length(),
        choices=Gender.choices(),
        default="Do not show"
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
