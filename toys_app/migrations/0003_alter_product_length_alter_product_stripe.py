# Generated by Django 4.2.7 on 2023-12-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toys_app", "0002_product_length_product_stripe_product_stripe_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="length",
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="stripe",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
