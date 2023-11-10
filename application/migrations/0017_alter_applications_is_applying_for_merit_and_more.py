# Generated by Django 4.2.5 on 2023-11-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0016_applications_applying_for_academic_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applications",
            name="is_applying_for_merit",
            field=models.BooleanField(
                default=False, help_text="SWA at least 1.75 equivalent to 88.75%)."
            ),
        ),
        migrations.AlterField(
            model_name="applications",
            name="scholarship_type",
            field=models.CharField(
                choices=[
                    ("BASIC PLUS SUC", "BASIC PLUS SUC"),
                    ("SUC_LCU", "SUC/LCU"),
                    ("BASIC SCHOLARSHIP", "BASIC SCHOLARSHIP"),
                    ("HONORS", "HONORS (FULL)"),
                    ("PRIORITY", "PRIORITY"),
                    ("PREMIER", "PREMIER"),
                ],
                default="BASIC SCHOLARSHIP",
                help_text="Kindly refer to the guidelines. Fraudulent inputs will deem your application as void.",
                max_length=20,
                null=True,
            ),
        ),
    ]
