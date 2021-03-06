# Generated by Django 3.2 on 2021-05-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_tournament_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='registration',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='rules',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='submission',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='timeline',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
