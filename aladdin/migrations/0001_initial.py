# Generated by Django 2.2.5 on 2021-04-26 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(help_text='Look up the ticker manually now', max_length=200, unique=True)),
                ('name', models.CharField(help_text='Enter a cryptocurrency name (e.g. Bitcoin)', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a portfolio name (e.g. Andras portfolio', max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_coins', models.DecimalField(decimal_places=0, max_digits=10)),
                ('trade_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aladdin.Coin')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aladdin.Portfolio')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioView',
            fields=[
                ('coin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aladdin.Coin')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aladdin.Portfolio')),
            ],
        ),
    ]
