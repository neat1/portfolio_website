# Generated by Django 2.2.5 on 2021-04-23 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aladdin', '0004_auto_20210423_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='coins',
        ),
    ]