# Generated by Django 4.0.6 on 2023-05-30 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_remove_student_image_path_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('student', 'course')},
        ),
    ]
