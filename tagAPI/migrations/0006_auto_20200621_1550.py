# Generated by Django 3.0.3 on 2020-06-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagAPI', '0005_auto_20200621_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='prediction',
            field=models.CharField(default='[]', max_length=100),
        ),
    ]
