from django.db import models

# Create your models here.


class inserir_instancias_tipo(models.Model):
    
    nome = models.TextField()
    classe = models.TextField()
    
    def __str__(self):
        return self.nome

class novo_instancias_tipo(models.Model):
    
    busca = models.TextField()
    
    def __str__(self):
        return self.busca
    # retorna o titulo como string para aparecer na listagem de posts