# Generated by Django 4.0.6 on 2023-03-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_subject_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='CSC 413', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
