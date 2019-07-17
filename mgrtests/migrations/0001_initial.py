# Generated by Django 2.2.3 on 2019-07-17 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('dbfaca19-a11d-4c12-a27c-cb9d0c8bc893'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('a33d6cd8-9e3e-4744-a4e7-2b15a6a9f0f0'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='mgrtests.Product')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_versions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('d3568a92-4af4-46ca-bb9c-2871f0f98dba'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suites', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suites', to='mgrtests.Product')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_suites', to=settings.AUTH_USER_MODEL)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suites', to='mgrtests.Version')),
            ],
        ),
        migrations.CreateModel(
            name='TestRuns',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('207af698-2e20-4a22-af06-42645b751eab'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('cases', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_runs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b9087a3a-8451-4a4f-b901-d7d4c4ceab21'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL)),
                ('suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='mgrtests.TestSuite')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_cases', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('c7706cfe-757a-4510-899c-c26e694c2a7c'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_tags', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('ea648fb1-b823-4b20-8eb0-246f146a12ca'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_components', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
