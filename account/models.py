from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    terms = models.BooleanField(default=True)
    address_1 = models.CharField(max_length=120, blank=True)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    studio_name = models.CharField(max_length=180, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
