# Generated by Django 3.0.1 on 2020-02-25 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200226_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]