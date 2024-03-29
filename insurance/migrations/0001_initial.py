# Generated by Django 5.0.2 on 2024-02-08 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_status_name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_type_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=11, unique=True)),
                ('validity_start_date', models.DateField()),
                ('validity_end_date', models.DateField()),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policystatus', verbose_name='Policy Status')),
                ('policy_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policytype', verbose_name='Policy Type')),
            ],
        ),
    ]
