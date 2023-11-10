# Generated by Django 4.1.7 on 2023-05-06 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0004_alter_carmodels_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('contact', models.BigIntegerField(default=False)),
                ('pickuptime', models.CharField(default=False, max_length=50)),
                ('tprice', models.BigIntegerField(default=None)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbconnection.carmodels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbconnection.registration')),
            ],
            options={
                'db_table': 'booking_table',
            },
        ),
    ]