# Generated by Django 3.0.1 on 2020-02-26 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0019_team_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='date',
            field=models.DateTimeField(blank=True, verbose_name=django.utils.timezone.now),
        ),
    ]
