# Generated by Django 4.0.6 on 2022-07-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
