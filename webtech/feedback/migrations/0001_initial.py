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
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('apartment_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('description', models.CharField(max_length=400, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]*$', 'Shall Contain only alphabets and numbers')])),
                ('rating', models.IntegerField(default=1)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
    ]
