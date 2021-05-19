from django.db import models


class Base (models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizar = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Livrob(Base):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    descricao = models.TextField(max_length=4000)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return '%s - %s' % (self.id, self.titulo)


class AvaliarLivro(Base):
    livro = models.ForeignKey(Livrob, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_length=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = "Avaliações"
        unique_together = ['email', 'livro']

        def __str__(self):
            return f'{self.nome} avaliou o livro {self.livro} com a nota {self.avaliacao}'
