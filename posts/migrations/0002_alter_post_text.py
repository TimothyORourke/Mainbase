# Generated by Django 3.2.4 on 2021-06-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=280),
        ),
    ]
