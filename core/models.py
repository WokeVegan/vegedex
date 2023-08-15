from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'bmp', 'webp'])
    ])
