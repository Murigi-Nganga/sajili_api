# Generated by Django 4.0.6 on 2023-04-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_lecturer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
