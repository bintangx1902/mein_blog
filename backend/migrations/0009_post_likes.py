# Generated by Django 3.2.7 on 2021-09-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_profile_nick_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
    ]
