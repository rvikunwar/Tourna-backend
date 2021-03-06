# Generated by Django 3.2 on 2021-05-10 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date_time', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('timeline', models.CharField(max_length=2000, null=True)),
                ('submission', models.CharField(max_length=2000, null=True)),
                ('rules', models.CharField(max_length=2000, null=True)),
                ('registration', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
