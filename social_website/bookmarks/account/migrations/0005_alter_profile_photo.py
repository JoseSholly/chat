# Generated by Django 4.1 on 2023-09-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='user/%Y/%m/%d/'),
        ),
    ]
