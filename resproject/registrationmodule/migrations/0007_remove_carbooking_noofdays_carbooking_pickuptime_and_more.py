# Generated by Django 4.1.7 on 2023-05-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmodule', '0006_carbooking_noofdays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbooking',
            name='noofdays',
        ),
        migrations.AddField(
            model_name='carbooking',
            name='pickuptime',
            field=models.CharField(choices=[('8:30', '8:30'), ('9:00', '9:00'), ('9:30', '9:30')], default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='carbooking',
            name='contact',
            field=models.BigIntegerField(default=False),
        ),
    ]
