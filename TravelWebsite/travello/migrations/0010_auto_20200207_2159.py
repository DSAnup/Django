# Generated by Django 3.0.1 on 2020-02-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0009_auto_20200207_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslider',
            name='img',
            field=models.ImageField(upload_to='homeslider'),
        ),
    ]
