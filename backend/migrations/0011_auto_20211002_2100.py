# Generated by Django 3.2.7 on 2021-10-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_create',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_update',
            field=models.DateField(auto_now=True),
        ),
    ]
