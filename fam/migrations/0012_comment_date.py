# Generated by Django 3.1.1 on 2020-10-30 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
