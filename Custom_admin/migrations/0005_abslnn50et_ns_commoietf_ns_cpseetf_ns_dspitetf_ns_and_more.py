# Generated by Django 4.0.2 on 2024-02-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_admin', '0004_alletf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABSLNN50ET_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='COMMOIETF_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CPSEETF_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DSPITETF_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EGOLD_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ICICIB22_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ITIETF_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MAFANG_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MOVALUE_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NIFITETF_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PSUBNKIETF_NS',
            fields=[
                ('date', models.DateField(default='-', primary_key=True, serialize=False)),
                ('Open', models.FloatField(default='-', null=True)),
                ('high', models.FloatField(default='-', null=True)),
                ('low', models.FloatField(default='-', null=True)),
                ('close', models.FloatField(default='-', null=True)),
                ('volume', models.BigIntegerField(default='-', null=True)),
                ('dividends', models.FloatField(default='-', null=True)),
                ('stock_splits', models.FloatField(default='-', null=True)),
            ],
        ),
    ]