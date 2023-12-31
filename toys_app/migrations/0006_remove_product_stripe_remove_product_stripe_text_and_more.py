# Generated by Django 4.2.7 on 2023-12-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toys_app", "0005_alter_product_length"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="stripe",
        ),
        migrations.RemoveField(
            model_name="product",
            name="stripe_text",
        ),
        migrations.AddField(
            model_name="purchase",
            name="stripe",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="purchase",
            name="stripe_text",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
