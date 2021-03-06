# Generated by Django 3.1.7 on 2021-03-22 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('futsal', '0002_auto_20210322_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_time',
            field=models.TimeField(),
        ),
    ]
