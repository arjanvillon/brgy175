# Generated by Django 2.2.5 on 2019-11-13 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0009_auto_20191113_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='residents.Resident'),
        ),
    ]
