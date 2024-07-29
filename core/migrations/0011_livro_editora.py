# Generated by Django 5.0.2 on 2024-07-29 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_livro_autor_livro_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="editora",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.editora",
            ),
        ),
    ]
