from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):

    name = models.CharField(
        max_length=30,
        null = False,
        blank = False,
    )
    personal_photo = models.URLField(
        blank=False,
        null=False,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(unique=True, editable=False)

    # in order to have your own representation of the object instead of "Pet object (1)"
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)


