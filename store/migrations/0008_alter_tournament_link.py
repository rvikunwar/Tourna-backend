# Generated by Django 3.2 on 2021-05-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_tournament_open_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
