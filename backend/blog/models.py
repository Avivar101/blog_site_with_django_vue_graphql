from django.db import models


class Profile(models.Model):
    user = models.OneToOneField
    website = None
    bio = None

    def __str__(self):
        return self.user.get_username()