# Generated by Django 3.1.1 on 2020-10-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0008_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
