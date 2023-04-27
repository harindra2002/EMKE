# Generated by Django 4.1 on 2023-04-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0019_alter_doctor_doctor_id_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_id',
            field=models.IntegerField(default=73698, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.IntegerField(default=64693, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterModelTable(
            name='doctor',
            table=None,
        ),
        migrations.AlterModelTable(
            name='patient',
            table=None,
        ),
    ]