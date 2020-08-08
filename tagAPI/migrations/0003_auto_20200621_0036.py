# Generated by Django 3.0.3 on 2020-06-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagAPI', '0002_auto_20200618_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('token', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.TextField(default='', max_length=100)),
                ('body', models.TextField(default='', max_length=400)),
                ('predicted', models.BooleanField(default=False)),
                ('prediction', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
