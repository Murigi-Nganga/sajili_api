# Generated by Django 4.0.6 on 2023-05-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_attendance_time_signed_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='method_used',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_signed_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
