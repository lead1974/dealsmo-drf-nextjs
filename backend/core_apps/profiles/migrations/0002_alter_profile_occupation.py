# Generated by Django 5.0.2 on 2025-01-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="occupation",
            field=models.CharField(
                choices=[
                    ("developer", "Developer"),
                    ("content_manager", "Content Manager"),
                    ("digital_marketing", "Digital Marketing"),
                    ("customer_support", "Customer Support"),
                    ("data_analyst", "Data Analyst"),
                    ("graphic_designer", "Graphic Designer"),
                    ("lega_compliance", "Legal Compliance"),
                    ("user", "User"),
                ],
                default="user",
                max_length=20,
                verbose_name="Occupation",
            ),
        ),
    ]
