# Generated by Django 3.2 on 2021-05-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210510_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='open_closed',
            field=models.CharField(choices=[('1', 'OPEN'), ('2', 'CLOSED')], default='1', max_length=20),
        ),
    ]
