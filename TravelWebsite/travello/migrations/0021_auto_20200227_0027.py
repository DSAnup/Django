# Generated by Django 3.0.1 on 2020-02-26 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0020_auto_20200227_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 27, 0, 27, 47, 942895)),
        ),
    ]
