# Generated by Django 3.1.1 on 2021-06-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_banner',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
