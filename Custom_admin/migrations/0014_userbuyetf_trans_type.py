# Generated by Django 4.2.6 on 2024-02-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_admin', '0013_userbuyetf_purchase_close_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbuyetf',
            name='trans_type',
            field=models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=20, null=True),
        ),
    ]
