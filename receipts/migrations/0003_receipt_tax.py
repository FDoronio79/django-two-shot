# Generated by Django 4.0.6 on 2022-07-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_alter_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='tax',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]