# Generated by Django 4.1.5 on 2023-01-18 22:44

import contact.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=contact.utils.pfp_handle),
        ),
    ]
