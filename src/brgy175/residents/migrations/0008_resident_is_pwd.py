# Generated by Django 2.2.5 on 2019-11-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0007_resident_senior_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='is_pwd',
            field=models.BooleanField(default=False),
        ),
    ]
