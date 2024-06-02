# Generated by Django 4.2.6 on 2024-02-26 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registeredUser', '0009_wallet'),
        ('Custom_admin', '0011_remove_userbuyetf_etf_purchased_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllETF',
            fields=[
                ('Etfnames', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('asset_type', models.CharField(choices=[('COMMODITIES', 'Commodities'), ('STOCKS', 'Stocks')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBuyetf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and Time')),
                ('Quantity', models.IntegerField(max_length=20, null=True)),
                ('Cost', models.IntegerField(max_length=20, null=True)),
                ('Etf_purchased', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Custom_admin.alletf')),
                ('Username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registeredUser.registereduser')),
            ],
        ),
    ]