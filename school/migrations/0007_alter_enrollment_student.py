# Generated by Django 4.0.6 on 2023-03-31 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_enrollment_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.student'),
        ),
    ]