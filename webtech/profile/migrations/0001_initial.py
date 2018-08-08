# Generated by Django 2.0.7 on 2018-08-08 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others'), ('N', 'Prefer Not to Mention')], max_length=1)),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator(message='Please check the email address')])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('(\\d{3}[-\\.\\s]??\\d{3}[-\\.\\s]??\\d{4}|\\(\\d{3}\\)\\s*\\d{3}[-\\.\\s]??\\d{4}|\\d{3}[-\\.\\s]??\\d{4})', 'Please check your phone number')])),
                ('university', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('branch', models.CharField(max_length=70, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('is_veg', models.CharField(choices=[('V', 'Vegetarian'), ('N', 'Non-Vegetarian')], max_length=1)),
                ('is_smoke', models.CharField(choices=[('S', 'Smoker'), ('N', 'Non-Smoker')], max_length=1)),
                ('is_alcohol', models.CharField(choices=[('A', 'Alcoholic'), ('N', 'Non-Alcoholic')], max_length=1)),
                ('profile_image', models.ImageField(default='images/jpeg/user.jpg', upload_to='images/')),
                ('credits', models.IntegerField(default=0, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Shall contain only numbers')])),
            ],
        ),
    ]