# Generated by Django 3.2.7 on 2021-09-25 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210925_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedia',
            name='icon',
        ),
    ]
