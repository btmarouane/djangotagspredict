# Generated by Django 3.0.3 on 2020-06-21 02:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagAPI', '0004_auto_20200621_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='prediction',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None),
        ),
    ]
