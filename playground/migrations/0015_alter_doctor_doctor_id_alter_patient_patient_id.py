# Generated by Django 4.2 on 2023-04-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0014_alter_doctor_doctor_id_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_id',
            field=models.IntegerField(default=46542, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.IntegerField(default=40104, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]