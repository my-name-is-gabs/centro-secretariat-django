# Generated by Django 4.2.5 on 2023-11-17 10:06

import application.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0029_alter_scholarprofile_scholarship_type"),
        ("application", "0034_alter_applications_applying_for_academic_year_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="applications",
            name="scholar",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scholar",
                to="accounts.scholar",
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