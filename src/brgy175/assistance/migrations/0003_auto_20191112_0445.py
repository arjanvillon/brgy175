# Generated by Django 2.2.7 on 2019-11-11 20:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0002_auto_20191112_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burial',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 20, 45, 59, 356512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 20, 45, 59, 356512, tzinfo=utc)),
        ),
    ]
