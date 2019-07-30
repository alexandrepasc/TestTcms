# Generated by Django 2.2.3 on 2019-07-30 19:43

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
                ('id', models.UUIDField(default=uuid.UUID('f9ff8146-b3db-4aca-8461-deb9c4f7e713'), primary_key=True, serialize=False, unique=True)),
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
                ('id', models.UUIDField(default=uuid.UUID('e10dd4d6-2fcc-446f-b088-461d08a5607d'), primary_key=True, serialize=False, unique=True)),
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
                ('id', models.UUIDField(default=uuid.UUID('cd5616c3-dfea-448a-98f3-e7b8c1a6c86f'), primary_key=True, serialize=False, unique=True)),
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
                ('id', models.UUIDField(default=uuid.UUID('f672c17c-b606-419e-b656-304151980fe1'), primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('actions', models.CharField(max_length=500000, null=True)),
                ('expected', models.CharField(max_length=500000, null=True)),
                ('notes', models.CharField(max_length=2000, null=True)),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField(null=True)),
                ('component', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='mgrtests.Component')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='mgrtests.Product')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='mgrtests.Tag')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update_cases', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('5d9ff07e-a3b4-4270-b3d0-187c49e91800'), primary_key=True, serialize=False, unique=True)),
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
                ('id', models.UUIDField(default=uuid.UUID('125a39b6-1a58-4d25-84e0-7bfadb556f84'), primary_key=True, serialize=False, unique=True)),
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
                ('id', models.UUIDField(default=uuid.UUID('3dcd67c6-08e7-4f1d-8c82-65fc8dc3c095'), primary_key=True, serialize=False, unique=True)),
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
                ('id', models.UUIDField(default=uuid.UUID('dda532dc-0cbd-4fd0-a79b-65a0f2150fde'), primary_key=True, serialize=False, unique=True)),
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
