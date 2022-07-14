from django.db import models

# Create your models here.

class novo_instancias_tipo(models.Model):
    
    CLASSES = (
        ('scrum:scrumRoles', 'Roles'),
        ('BPO__Activity', 'BPO__Activity'),
        ('KIPCO__Knowledge_Intensive_Activity', 'KIPCO__Knowledge_Intensive_Activity'),
        ('scrum_Daily', 'scrum_Daily'),
        ('BPO__Association', 'BPO__Association'), 
        ('BPO__Data_Object', 'BPO__Data_Object'),
        ('BPO__Flow', 'BPO__Flow'),
        ('Product_Backlog', 'Product_Backlog'),
        ('BPO__Message_Flow', 'BPO__Message_Flow'),
        ('KIPCO__Message_Flow', 'KIPCO__Message_Flow'),
        ('Product_RoadMap_Creation', 'Product_RoadMap_Creation'),
        ('Sprint_Backlog', 'Sprint_Backlog'),
        ('Vision_Creation', 'Vision_Creation'),
        ('BRO__Derivation_Foundational_Rule', 'BRO__Derivation_Foundational_Rule'),
        ('BRO__Foundational_Conclusion', 'BRO__Foundational_Conclusion'),
        ('BRO__Foundational_Condition', 'BRO__Foundational_Condition'),
        ('BRO__Foundational_Event', 'BRO__Foundational_Event'),
        ('BRO__Foundational_Integrity_Rule', 'BRO__Foundational_Integrity_Rule'),
        ('BRO__Foundational_Post_Condition', 'BRO__Foundational_Post_Condition'),
        ('BRO__Foundational_Business_Rule', 'BRO__Foundational_Business_Rule'),
        ('BRO__Reaction_Foundational_Rule', 'BRO__Reaction_Foundational_Rule'),
        ('KIPCO__Derivation_Rule', 'KIPCO__Derivation_Rule'),
        ('KIPCO__Integrity_Rule', 'KIPCO__Integrity_Rule'),
        ('KIPCO__Reaction_Rule', 'KIPCO__Reaction_Rule'),
        ('KIPCO__Business_Rule', 'KIPCO__Business_Rule'),
        ('DO__Criterion', 'DO__Criterion'),
        ('DO__Restriction', 'DO__Restriction'),
        #('', ''),
    )
    
    busca = models.CharField(max_length=255, choices=CLASSES)
    
    def __str__(self):
        return self.nome
    # retorna o titulo como string para aparecer na listagem de posts