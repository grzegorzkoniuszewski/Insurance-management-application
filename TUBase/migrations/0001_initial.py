# Generated by Django 5.0.2 on 2024-02-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTUBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('address_street', models.CharField(max_length=255)),
                ('address_building_number', models.CharField(max_length=20)),
                ('address_postal_code', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('id_name', models.CharField(max_length=3, unique=True)),
            ],
        ),
    ]
