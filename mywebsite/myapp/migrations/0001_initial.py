# Generated by Django 3.0.7 on 2021-05-22 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.TextField()),
                ('Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 22, 13, 26, 11, 687340))),
            ],
            options={
                'verbose_name_plural': 'Contact Us Form',
            },
        ),
    ]