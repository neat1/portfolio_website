# Generated by Django 2.2.5 on 2021-04-26 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aladdin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='cutip',
            new_name='coin',
        ),
    ]
