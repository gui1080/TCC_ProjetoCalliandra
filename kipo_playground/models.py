from django.db import models

# Create your models here.

class novo_instancias_tipo(models.Model):
    
    CLASSES = (
        ('Roles', 'Roles'),
        ('KIPCOAgent', 'KIPCOAgent') 
    )
    
    busca = models.CharField(max_length=255, choices=CLASSES)
    
    def __str__(self):
        return self.nome
    # retorna o titulo como string para aparecer na listagem de posts