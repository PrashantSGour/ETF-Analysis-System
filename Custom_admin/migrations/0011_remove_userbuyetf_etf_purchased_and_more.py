# Generated by Django 4.2.6 on 2024-02-26 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_admin', '0010_userbuyetf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AllETF',
        ),
        migrations.DeleteModel(
            name='UserBuyetf',
        ),
    ]
