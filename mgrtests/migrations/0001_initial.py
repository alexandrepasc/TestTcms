# Generated by Django 2.2.3 on 2019-07-21 22:05

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
            name='Component',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('80378ba5-f61a-495f-9e17-df7142450640'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_components', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('bf0dd4d8-62bf-47aa-9a2e-ff74cbdbfaa1'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('b70f16ee-f7aa-4f3c-aab2-b80fb8f21b1f'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_tags', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('f9a1c1c1-dc6e-4c5e-bddc-457413e20f04'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_cases', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('bb7c2bd5-edc6-4131-b990-9d7ce2160ba4'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suites', to='mgrtests.Component')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suites', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suites', to='mgrtests.Product')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suites', to='mgrtests.Tag')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_suites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('13393efd-e0a2-4da8-8668-b2e2669c1fe2'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='mgrtests.Product')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_versions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestSuitesCases',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('571b48f6-8ac4-4472-bf7a-da68a7bd4e46'), primary_key=True, serialize=False, unique=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_suites', to='mgrtests.TestCase')),
                ('suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suite_cases', to='mgrtests.TestSuite')),
            ],
        ),
        migrations.AddField(
            model_name='testsuite',
            name='version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suites', to='mgrtests.Version'),
        ),
        migrations.CreateModel(
            name='TestRuns',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('062e7201-c98d-4973-97b6-733cf3bfd3be'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('cases', models.TextField()),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_runs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
