# Generated by Django 3.0.1 on 2020-02-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_besttrip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testominal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=80)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
    ]
