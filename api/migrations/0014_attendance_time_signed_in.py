# Generated by Django 4.0.6 on 2023-05-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_attendance_method_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='time_signed_in',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]