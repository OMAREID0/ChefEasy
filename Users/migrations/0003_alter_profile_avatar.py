# Generated by Django 5.0.4 on 2024-05-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_profile_addres_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]