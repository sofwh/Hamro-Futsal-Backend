# Generated by Django 3.1.7 on 2021-04-06 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_forgotpasswordpin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email_verify',
        ),
    ]
