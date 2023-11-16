# Generated by Django 4.2.5 on 2023-11-13 13:03

import application.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0027_remove_applications_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applications",
            name="application_uuid",
        ),
        migrations.AddField(
            model_name="applications",
            name="application_reference_id",
            field=models.CharField(max_length=20, null=True),
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
