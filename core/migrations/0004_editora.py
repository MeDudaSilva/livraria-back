# Generated by Django 5.0.2 on 2024-03-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_categoria_descricao"),
    ]

    operations = [
        migrations.CreateModel(
            name="Editora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
