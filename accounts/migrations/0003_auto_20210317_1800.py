# Generated by Django 3.1.7 on 2021-03-17 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210316_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='user_role',
            field=models.CharField(choices=[('USER', 'User'), ('OWNER', 'Owner')], max_length=10),
        ),
    ]
