# Generated by Django 3.1.2 on 2021-05-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aladdin', '0004_auto_20210514_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='computed',
            field=models.DecimalField(decimal_places=0, default='10', max_digits=10),
        ),
    ]
