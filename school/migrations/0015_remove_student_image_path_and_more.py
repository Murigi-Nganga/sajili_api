# Generated by Django 4.0.6 on 2023-05-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_rename_course_id_enrollment_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image_path',
        ),
        migrations.AddField(
            model_name='student',
            name='face_image_encodings',
            field=models.CharField(max_length=8000, null=True),
        ),
    ]