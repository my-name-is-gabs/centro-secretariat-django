# Generated by Django 4.2.5 on 2023-10-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0003_remove_applications_is_archived_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applications",
            name="elementary_school_address",
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="applications",
            name="jhs_school_address",
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="applications",
            name="shs_school_address",
            field=models.TextField(max_length=100, null=True),
        ),
    ]
