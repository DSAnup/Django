# Generated by Django 3.0.1 on 2020-02-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0014_auto_20200216_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='homestatic',
            name='copyrighttext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
