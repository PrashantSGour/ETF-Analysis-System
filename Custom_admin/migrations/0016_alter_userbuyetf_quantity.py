# Generated by Django 4.2.6 on 2024-02-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_admin', '0015_alter_userbuyetf_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbuyetf',
            name='Quantity',
            field=models.FloatField(max_length=20, null=True),
        ),
    ]
