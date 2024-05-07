from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
