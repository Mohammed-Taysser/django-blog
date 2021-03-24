from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.


class UserProfile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='users_photos/%Y/%m/%d/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.thumbnail((300, 300))
        img.save(self.image.path)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
