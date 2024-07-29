from django.db import models
from .categoria import Categoria
from .editora import Editora

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbt = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros", null=True, blank=False
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True
    )

    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.quantidade})"