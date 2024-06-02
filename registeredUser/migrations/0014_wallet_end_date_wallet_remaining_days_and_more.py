# Generated by Django 4.2.6 on 2024-04-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeredUser', '0013_alter_wallet_sub_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='remaining_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wallet',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and Time'),
        ),
    ]
