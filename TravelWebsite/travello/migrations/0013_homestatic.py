# Generated by Django 3.0.1 on 2020-02-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0012_footercontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testiBackground', models.ImageField(upload_to='others')),
                ('bestSide', models.ImageField(upload_to='others')),
                ('footerBack', models.ImageField(upload_to='others')),
            ],
        ),
    ]
