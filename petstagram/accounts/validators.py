from django.core.exceptions import ValidationError

def only_alpha_validator(value):
    if not value.isalpha():
        raise ValidationError("Name must contain only letters!")
