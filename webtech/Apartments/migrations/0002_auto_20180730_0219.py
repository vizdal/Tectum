# Generated by Django 2.0.7 on 2018-07-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apartments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='available_units',
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment_image',
            field=models.ImageField(default='images/svg/apartment8.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='near_by',
            field=models.CharField(choices=[('DAL', 'Dalhousie university'), ('SMU', 'SMU university'), ('WALMART', 'Walmart-Mumfford'), ('COSTCO', 'Costco')], default='DAL', max_length=10),
        ),
        migrations.AddField(
            model_name='apartment',
            name='posession',
            field=models.CharField(choices=[('<1', 'Less than month'), ('1-2', '1-2 month')], default='<1', max_length=10),
        ),
        migrations.AddField(
            model_name='apartment',
            name='sharing',
            field=models.CharField(choices=[('Y', 'Sharing'), ('N', 'No-Sharing')], default='Y', max_length=1),
        ),
        migrations.AddField(
            model_name='apartment',
            name='type_of_room',
            field=models.CharField(choices=[('1', '1BHK'), ('2', '2BHK'), ('3', '3BHK'), ('B', 'Bungalow'), ('S', 'Single Room')], default='2', max_length=10),
        ),
    ]
