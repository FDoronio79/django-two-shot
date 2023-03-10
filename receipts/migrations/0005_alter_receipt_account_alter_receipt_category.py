# Generated by Django 4.0.6 on 2022-07-28 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0004_alter_receipt_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='receipts.account'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='receipts.expensecategory'),
        ),
    ]
