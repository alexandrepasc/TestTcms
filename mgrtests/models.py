import uuid
from django.db import models
from django.contrib.auth.models import User


class TestSuite(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='suites', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TestCase(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    suite = models.ForeignKey(TestSuite, related_name='cases', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='cases', on_delete=models.CASCADE)


class TestRuns(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    cases = models.TextField()
    created_by = models.ForeignKey(User, related_name='runs', on_delete=models.CASCADE)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)


class Version(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='versions', on_delete=models.CASCADE)
