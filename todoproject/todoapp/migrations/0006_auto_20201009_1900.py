# Generated by Django 3.1.2 on 2020-10-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_auto_20201009_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(),
        ),
    ]
