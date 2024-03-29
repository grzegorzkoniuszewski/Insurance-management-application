# Generated by Django 5.0.2 on 2024-02-26 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_alter_insurancepolicy_options_and_more'),
        ('vehicle', '0002_vehiclestatus_alter_customvehicle_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclestatus',
            name='vehicle_status_name',
        ),
        migrations.AddField(
            model_name='customvehicle',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.vehiclestatus', verbose_name='Vehicle Status'),
        ),
        migrations.AddField(
            model_name='vehiclestatus',
            name='vehicle_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policystatus'),
        ),
    ]
