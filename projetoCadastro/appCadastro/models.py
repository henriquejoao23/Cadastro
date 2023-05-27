from django.db import models

# Create your models here.

class Produto(models.Model):
    idProduto = models.AutoField(primary_key=True)
    nome = models.TextField(max_Lenght=255)
    descricao =models.TextField(max_Lenght=255)
    preco = models.FloatField()
    validade = models.DateField()

# create table produto  
