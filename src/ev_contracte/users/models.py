from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return '{} Profile'.format(self.user.username)

#     def save(self):
#         super().save()

        # img = image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)