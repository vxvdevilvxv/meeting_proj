from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Name')
    last_name = models.CharField(max_length=150, verbose_name='Surname')
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, verbose_name='Gender')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', height_field=200, width_field=200, blank=True,
                               verbose_name='Avatar')
    email = models.EmailField(max_length=250, verbose_name='Email')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'


class Gender(models.Model):
    gender = models.CharField(max_length=20, verbose_name='Gender')
