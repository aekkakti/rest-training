from django.contrib.auth.models import AbstractUser
from django.db import models

class AdvUser(AbstractUser):
    class Meta:
        pass

class Product(models.Model):
    name = models.TextField(max_length=50, verbose_name='Название товара')
    description = models.TextField(max_length=300, verbose_name='Описание товара')
    photo = models.ImageField(upload_to='media/', verbose_name='Фото товара')

    def __str__(self):
        return self.name
