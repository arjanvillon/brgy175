# Generated by Django 2.2.5 on 2019-11-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0003_remove_resident_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='age',
            field=models.CharField(default='age', max_length=4),
        ),
    ]