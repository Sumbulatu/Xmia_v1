from django.db import models

class UserProfile(models.Model):
    uid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
