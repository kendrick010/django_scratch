# Generated by Django 5.0.7 on 2024-07-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]