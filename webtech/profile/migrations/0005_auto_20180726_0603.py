# Generated by Django 2.0.7 on 2018-07-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20180726_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='static/images/jpeg/user.jpg', upload_to='images/'),
        ),
    ]