# Generated by Django 5.0.2 on 2024-07-29 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_livro_editora"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="autor",
        ),
    ]
