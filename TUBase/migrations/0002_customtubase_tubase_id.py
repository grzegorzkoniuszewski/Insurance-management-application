# Generated by Django 5.0.2 on 2024-03-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TUBase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtubase',
            name='tuBase_id',
            field=models.CharField(max_length=99, null=True),
        ),
    ]