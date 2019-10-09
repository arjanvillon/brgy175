# Generated by Django 2.2.5 on 2019-10-09 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
        ('residents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='burialForm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.BurialForm'),
        ),
        migrations.AddField(
            model_name='resident',
            name='businessPermit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.BusinessPermit'),
        ),
        migrations.AddField(
            model_name='resident',
            name='clearanceForm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.ClearanceForm'),
        ),
        migrations.AddField(
            model_name='resident',
            name='idForm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.IDForm'),
        ),
        migrations.AddField(
            model_name='resident',
            name='scholarshipForm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.ScholarshipForm'),
        ),
    ]
