# Generated by Django 3.2 on 2021-05-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210510_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='open_closed',
            field=models.CharField(choices=[('1', 'OPEN'), ('2', 'CLOSED')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='tournament',
            name='prize',
            field=models.IntegerField(null=True),
        ),
    ]
