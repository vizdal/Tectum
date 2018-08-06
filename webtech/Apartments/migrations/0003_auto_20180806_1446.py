# Generated by Django 2.0.7 on 2018-08-06 14:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0002_auto_20180806_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='apartment_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Shall contain only numerals')]),
        ),
    ]