# Generated by Django 4.2.5 on 2023-10-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demographics", "0008_remove_applicant_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="applicant",
            name="testField",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]