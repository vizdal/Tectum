# Generated by Django 2.0.7 on 2018-08-04 05:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartment_id', models.AutoField(primary_key=True, serialize=False)),
                ('apartment_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('available_units', models.IntegerField(default=0, validators=[django.core.validators.RegexValidator('^[0-9]$', 'Shall contain only numerals')])),
                ('apartment_location', models.CharField(max_length=400, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('apartment_description', models.CharField(max_length=400, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('apartment_price', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9]$', 'Shall contain only numerals')])),
                ('near_by', models.CharField(choices=[('DAL', 'Dalhousie university'), ('SMU', 'SMU university'), ('WALMART', 'Walmart-Mumfford'), ('COSTCO', 'Costco')], default='DAL', max_length=10)),
                ('type_of_room', models.CharField(choices=[('1', '1BHK'), ('2', '2BHK'), ('3', '3BHK'), ('B', 'Bungalow'), ('S', 'Single Room')], default='2', max_length=10)),
                ('posession', models.BigIntegerField(default=0, validators=[django.core.validators.RegexValidator('^[0-9]$', 'Shall contain only numerals')])),
                ('sharing', models.CharField(choices=[('Y', 'Sharing'), ('N', 'No-Sharing')], default='N', max_length=1)),
                ('apartment_image', models.ImageField(default='images/svg/apartment.svg', upload_to='images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='owner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]$', 'Shall contain only alphabets')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]$', 'Shall contain only alphabets')])),
                ('email', models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator(message='Please check the email address')])),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('(\\d{3}[-\\.\\s]??\\d{3}[-\\.\\s]??\\d{4}|\\(\\d{3}\\)\\s*\\d{3}[-\\.\\s]??\\d{4}|\\d{3}[-\\.\\s]??\\d{4})', 'Please check your phone number')])),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
            ],
        ),
    ]
