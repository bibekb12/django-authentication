# Generated by Django 5.1.4 on 2025-01-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=200)),
            ],
        ),
    ]
