# Generated by Django 4.2.5 on 2023-11-19 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("index", "0004_alter_passwordreset_expires_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passwordreset",
            name="expires_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 19, 11, 35, 15, 60572, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]