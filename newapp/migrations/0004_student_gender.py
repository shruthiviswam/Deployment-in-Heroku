# Generated by Django 3.0.6 on 2020-06-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20200601_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='NA', max_length=10),
        ),
    ]
