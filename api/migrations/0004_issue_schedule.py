# Generated by Django 4.0.6 on 2023-04-08 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_center_lat_location_centre_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.schedule'),
        ),
    ]
