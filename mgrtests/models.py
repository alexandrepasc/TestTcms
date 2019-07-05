from django.db import models
from django.contrib.auth.models import User


class TestSuite(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
