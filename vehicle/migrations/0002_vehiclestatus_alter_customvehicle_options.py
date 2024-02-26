# Generated by Django 5.0.2 on 2024-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_status_name', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'verbose_name': 'Vehicle status',
                'verbose_name_plural': 'Vehicle statuses',
            },
        ),
        migrations.AlterModelOptions(
            name='customvehicle',
            options={'verbose_name': 'Vehicle', 'verbose_name_plural': 'Vehicle'},
        ),
    ]