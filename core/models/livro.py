from django.db import models

from uploader.models import Image

from .autor import Autor
from .categoria import Categoria
from .editora import Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbt = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", null=True, blank=False)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    # autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros_autor", blank=True, null=True)
    # coautor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros_coautor", blank=True, null=True)
    autores = models.ManyToManyField(Autor, related_name="livros", blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"({self.id}) R${self.preco} - {self.titulo} - CATEGORIA:{self.categoria} - EDITORA:{self.editora} - ({self.quantidade})"
