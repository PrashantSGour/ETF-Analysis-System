# Generated by Django 4.2.6 on 2024-02-28 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_admin', '0014_userbuyetf_trans_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbuyetf',
            name='Cost',
            field=models.FloatField(max_length=20, null=True),
        ),
    ]