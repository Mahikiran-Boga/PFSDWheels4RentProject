# Generated by Django 4.1.7 on 2023-05-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconnection', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
