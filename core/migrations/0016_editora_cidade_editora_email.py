# Generated by Django 5.0.2 on 2024-08-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_livro_capa"),
    ]

    operations = [
        migrations.AddField(
            model_name="editora",
            name="cidade",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
