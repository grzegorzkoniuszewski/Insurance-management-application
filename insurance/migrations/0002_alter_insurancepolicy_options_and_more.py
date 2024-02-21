# Generated by Django 5.0.2 on 2024-02-21 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUBase', '0001_initial'),
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='insurancepolicy',
            options={'verbose_name': 'Insurance policy', 'verbose_name_plural': 'Insurance policies'},
        ),
        migrations.AlterModelOptions(
            name='policystatus',
            options={'verbose_name': 'Policy status', 'verbose_name_plural': 'Policy statuses'},
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='insurance_company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TUBase.customtubase', verbose_name='Insurance Company'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='policy_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policytype', verbose_name='Policies Type'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='insurance.policystatus', verbose_name='Policies Status'),
        ),
    ]
