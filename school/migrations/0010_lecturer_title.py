# Generated by Django 4.0.6 on 2023-04-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_alter_admin_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='title',
            field=models.CharField(default='Mr', max_length=255),
        ),
    ]
