from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from owlready2 import *         # https://pypi.org/project/Owlready2/

# Create your views here.

def welcome(request):
    
    return render(request, 'welcome.html')

def instancias_teste(request):

    '''     
    Resolve SQLite Locked Error

    To fix “SQLite database is locked error code 5” the best solution is to 
    create a backup of the database, which will have no locks on it. 
    After that, replace the database with its backup copy. 
    
    Follow the following script to do the same where 
    .x.Sqlite is the Sqlite database file:
    
    - $Sqlite3 .x.Sqlite
    - Sqlite> .backup main backup.Sqlite
    - Sqlite> .exit
'''
        
    myworld = World(filename='backup.db', exclusive=False)
        
    onto_path.append(os.path.dirname(__file__))
        
    # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
    kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum.owl').load()
        
    myworld.save()
    # Sincronização
    #--------------------------------------------------------------------------
        
    print("\n------------------------------------\n")
    print("Sincronização!")
        
    try:
        sync_reasoner()
    except:
        print("\n\nErro ao sincronizar.\n\n")
    finally:
        print("\n\nSincronização finalizada.\n\n")    
        
    print("\n------------------------------------\n")
    
    print("\nsubject rdfs:subClassOf ?object\n")
    
    query_feita = "subject rdfs:subClassOf ?object"
    
    lista_intancias = list(myworld.sparql("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            SELECT ?subject ?object WHERE{ 
                ?subject rdfs:subClassOf ?object.
                ?object rdf:type owl:Class.
            }
    """)) 
    
    del myworld, kiposcrum    
        
    contexto = {"lista_intancias": lista_intancias, "query_feita": query_feita}
    
    return render(request, 'instancias.html', contexto)