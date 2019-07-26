import uuid
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_products', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class Version(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='versions', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_versions', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_tags', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='components', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_components', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class TestSuite(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='suites', on_delete=models.CASCADE, null=True)
    version = models.ForeignKey(Version, related_name='suites', on_delete=models.CASCADE, null=True)
    component = models.ForeignKey(Component, related_name='suites', on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(Tag, related_name='suites', on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, related_name='suites', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_suites', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class TestCase(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    # suite = models.ForeignKey(TestSuite, related_name='cases', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='cases', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_cases', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)


class TestSuitesCases(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    suite = models.ForeignKey(TestSuite, related_name='suite_cases', on_delete=models.CASCADE)
    case = models.ForeignKey(TestCase, related_name='case_suites', on_delete=models.CASCADE)


class TestRuns(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4())
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cases = models.TextField()
    created_by = models.ForeignKey(User, related_name='runs', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.BigIntegerField()
    updated_by = models.ForeignKey(User, related_name='update_runs', on_delete=models.CASCADE, null=True)
    # updated_at = models.DateTimeField(null=True)
    updated_at = models.BigIntegerField(null=True)
