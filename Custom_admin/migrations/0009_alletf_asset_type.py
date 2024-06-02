# Generated by Django 5.0 on 2024-02-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Custom_admin", "0008_merge_20240218_2110"),
    ]

    operations = [
        migrations.AddField(
            model_name="alletf",
            name="asset_type",
            field=models.CharField(
                choices=[("COMMODITIES", "Commodities"), ("STOCKS", "Stocks")],
                max_length=20,
                null=True,
            ),
        ),
    ]
