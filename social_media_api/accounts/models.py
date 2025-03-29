from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# start task 0

class Customuser(AbstractUser):
    bio = models.TextField(max_length=600, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self',symmetrical=False, blank=True)


    def __str__(self):
        return self.username
# end task 0

# start task 2

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follow', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Customuser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Customuser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# end task 2
