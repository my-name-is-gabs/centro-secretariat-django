# Generated by Django 4.2.5 on 2023-11-10 14:52

import application.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0019_applications_course_duration_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eligibilityconfig",
            name="academic_year",
        ),
        migrations.AddField(
            model_name="eligibilityconfig",
            name="applying_for_academic_year",
            field=application.models.AcademicYearField(
                default=application.models.AcademicYearField.calculate_academic_year,
                editable=False,
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="applications",
            name="applying_for_academic_year",
            field=application.models.AcademicYearField(
                default=application.models.AcademicYearField.calculate_academic_year,
                editable=False,
                max_length=9,
            ),
        ),
    ]
