# Generated by Django 4.0.6 on 2023-03-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_remove_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
