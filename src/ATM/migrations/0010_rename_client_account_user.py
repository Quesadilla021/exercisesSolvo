# Generated by Django 5.0 on 2024-08-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0009_alter_account_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='client',
            new_name='user',
        ),
    ]
