# Generated by Django 4.2.5 on 2023-10-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0004_alter_applications_elementary_school_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applications",
            name="guardians_voter_certificate",
            field=models.FileField(
                help_text="Insert one of your guardian's voter certificate (for verification and validation purposes).",
                null=True,
                upload_to="guardian/voters_certificate",
            ),
        ),
        migrations.AlterField(
            model_name="applications",
            name="shiftee",
            field=models.CharField(
                default="N/A",
                help_text="Title of your previous course (if shiftee).",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="applications",
            name="transferee",
            field=models.CharField(
                default="N/A",
                help_text="Name of your previous school/university.",
                max_length=50,
                null=True,
            ),
        ),
    ]