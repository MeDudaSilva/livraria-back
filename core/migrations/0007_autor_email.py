# Generated by Django 5.0.2 on 2024-03-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_autor"),
    ]

    operations = [
        migrations.AddField(
            model_name="autor",
            name="email",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
