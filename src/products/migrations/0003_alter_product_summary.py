# Generated by Django 5.0.7 on 2024-07-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="summary",
            field=models.TextField(blank=True, null=True),
        ),
    ]
