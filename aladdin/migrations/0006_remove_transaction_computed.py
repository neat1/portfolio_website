# Generated by Django 3.1.2 on 2021-05-24 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aladdin', '0005_transaction_computed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='computed',
        ),
    ]
