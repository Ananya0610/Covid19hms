# Generated by Django 4.0.3 on 2022-05-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chms', '0003_alter_appointment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='sdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shift',
            name='stime',
            field=models.TimeField(),
        ),
    ]
