# Generated by Django 4.2.5 on 2023-11-14 05:06

import application.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0029_alter_applications_applying_for_academic_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applications",
            name="applying_for_academic_year",
            field=application.models.AcademicYearField(
                default=application.models.AcademicYearField.calculate_academic_year,
                editable=False,
                max_length=9,
            ),
        ),
        migrations.AlterField(
            model_name="eligibilityconfig",
            name="applying_for_academic_year",
            field=application.models.AcademicYearField(
                default=application.models.AcademicYearField.calculate_academic_year,
                editable=False,
                max_length=9,
            ),
        ),
    ]
