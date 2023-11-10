# Generated by Django 4.1.7 on 2023-05-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmodule', '0009_carbooking_tprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('query', models.TextField(default=False)),
            ],
            options={
                'db_table': 'contact_table',
            },
        ),
    ]
