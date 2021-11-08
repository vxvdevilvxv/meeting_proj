from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    first_name = models.CharField(max_length=150, verbose_name='Name')
    last_name = models.CharField(max_length=150, verbose_name='Surname')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, verbose_name='Gender')
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,
                               verbose_name='Avatar')
    email = models.EmailField(max_length=250, verbose_name='Email')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
