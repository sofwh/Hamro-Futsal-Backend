# Generated by Django 3.1.7 on 2021-03-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futsal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=20)),
                ('book_date', models.DateTimeField(auto_now_add=True)),
                ('book_time', models.TimeField(auto_now_add=True)),
                ('book_fut_type', models.CharField(choices=[('7A', '7A'), ('5A', '5A')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='futsal',
            name='fut_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='futsal',
            name='fut_phone',
            field=models.CharField(default='52152', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='futsal',
            name='futsal_rate',
            field=models.PositiveIntegerField(default=0),
        ),
    ]