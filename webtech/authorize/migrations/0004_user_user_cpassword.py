# Generated by Django 2.0.7 on 2018-08-07 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0003_auto_20180807_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_cpassword',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]