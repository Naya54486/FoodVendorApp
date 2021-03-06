# Generated by Django 2.2 on 2020-05-29 21:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200528_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='order',
            name='cancel_expiry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 29, 21, 21, 41, 173636, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 29, 21, 11, 41, 173636, tzinfo=utc)),
        ),
    ]
