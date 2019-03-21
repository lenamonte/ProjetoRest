from django.db import models

# Create your models here.


class Livro(models.Model):

    class Meta:

        db_table = 'livro'

    titulo = models.CharField(max_length=200)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo
