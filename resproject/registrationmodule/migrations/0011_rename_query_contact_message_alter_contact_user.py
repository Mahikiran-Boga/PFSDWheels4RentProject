# Generated by Django 4.1.7 on 2023-05-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationmodule', '0010_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='query',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.CharField(default=False, max_length=50, unique=True),
        ),
    ]
