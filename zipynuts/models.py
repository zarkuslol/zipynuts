from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    preço = models.CharField(max_length=20)
    quantidade = models.CharField(max_length=20)
    peso_em_gramas = models.CharField(max_length=20)
    data_de_fabricação = models.CharField(max_length=20)
    data_de_validade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
