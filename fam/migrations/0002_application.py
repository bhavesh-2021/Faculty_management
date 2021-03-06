# Generated by Django 3.1.1 on 2020-10-25 09:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
