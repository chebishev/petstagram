from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size

UserModel = get_user_model()


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=(validate_file_size,))
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],  # this validator is accessible after import
        blank=True,
        null=True,
    )
    location = models.TextField(
        max_length=30,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet, blank=True
    )
    date_of_publication = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)