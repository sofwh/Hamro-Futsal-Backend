# Generated by Django 3.1.7 on 2021-03-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futsal', '0018_userbooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='member_type',
            field=models.CharField(choices=[('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond')], max_length=20),
        ),
    ]
