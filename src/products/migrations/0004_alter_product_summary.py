# Generated by Django 5.0.7 on 2024-07-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_alter_product_summary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="summary",
            field=models.TextField(null=True),
        ),
    ]
