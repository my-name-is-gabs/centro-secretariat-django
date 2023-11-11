# Generated by Django 4.2.5 on 2023-11-10 14:15

import application.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0017_alter_applications_is_applying_for_merit_and_more"),
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
            model_name="applications",
            name="years_of_residency",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="eligibilityconfig",
            name="academic_year",
            field=application.models.AcademicYearField(
                default=application.models.AcademicYearField.calculate_academic_year,
                editable=False,
                max_length=9,
            ),
        ),
    ]