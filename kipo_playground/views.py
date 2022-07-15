from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm, inserir_instancias_tipoForm
from owlready2 import *         # https://pypi.org/project/Owlready2/
import re

# source venv/bin/activate
# python3 manage.py runserver

# Create your views here.

def welcome(request):
    
    return render(request, 'welcome.html')

# mostra o input de todas as instâncias de dada classe
def instancias_tipo_show(request):
    
    return render(request, 'instancias_tipo_show.html')

# seleciona classe para ver
def instancias_tipo(request):
    
    form = novo_instancias_tipoForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'input_dado' in request.session:
            del request.session['input_dado']
    
        input_dado = request.POST.get('busca')
        
        print(input_dado)
        
        # OWLREADY2
        
        myworld = World(filename='backup.db', exclusive=False)
        
        onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum_pellet.owl').load()
        
        try:
        
            with kiposcrum:
                
                busca = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX scrum: <http://www.semanticweb.org/fialho/kipo#>
                    SELECT *
                    WHERE {
                        ?cls rdfs:subClassOf* """+ str(input_dado) +""".
                        ?individual a ?cls.
                    }
                """
                    
                lista_intancias = list(myworld.sparql(busca)) 
            
                print(lista_intancias)
                
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
                
        
                myworld.save()
        
        except:
            
            print("Falha de acesso!")
        
        del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_dado'] = str(lista_intancias)
        return redirect('/kipo_playground/instancias_tipo_show/')
    
    return render(request, 'instancias_tipo_select.html', context)

# instancia pra botar + espaço pra definir o nome
def inserir_instancia(request):

    form = inserir_instancias_tipoForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'input_dado' in request.session:
            del request.session['input_dado']
    
        input_nome = request.POST.get('nome')
        input_classe = request.POST.get('classe')
        
        print(input_nome)
        print(input_classe)
        
        
        # OWLREADY2
        
        myworld = World(filename='backup.db', exclusive=False)
        
        onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum_pellet.owl').load()
        
        
        try:
        
            with kiposcrum:
                
                busca = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX scrum: <http://www.semanticweb.org/fialho/kipo#>
                    INSERT DATA {
                        """ + str(input_nome) + """ rdf:type """ + str(input_classe) + """.
                    }
                """
                    
                lista_intancias = list(myworld.sparql(busca)) 
            
                print(lista_intancias)
                
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
                
        
                myworld.save()
        
        except:
            
            print("Falha de acesso!")
        
        del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_nome'] = input_nome
        request.session['input_classe'] = input_classe
        request.session['input_status'] = "placeholder"
        return redirect('/kipo_playground/inserir_instancia_tela_ok/')
        
    
    return render(request, 'instancias_inserir_select.html', context)

def inserir_instancia_tela_ok(request):
    # menu de mostrar instancia pra botar + espaço pra definir o nome
    return render(request, 'inserir_instancia_tela_ok.html')


def instancias_teste(request):
        
    myworld = World(filename='backup.db', exclusive=False)
        
    onto_path.append(os.path.dirname(__file__))
        
    # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
    kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum_pellet.owl').load()
    
    print("\nsubject rdfs:subClassOf ?object\n")
    
    query_feita = "subject rdfs:subClassOf ?object"
    
    # se não for nessa estrutura, dá TABLE LOCKED!
    try:
        
        with kiposcrum:
                
                
            busca = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    SELECT ?subject ?object WHERE{ 
                        ?subject rdfs:subClassOf ?object.
                        ?object rdf:type owl:Class.
                    }
            """
                
            lista_intancias = list(myworld.sparql(busca)) 
            
            busca = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    SELECT (COUNT(*) AS ?no) 
                    WHERE { ?s ?p ?o  }
            """
                
            quantidade_triplets = list(myworld.sparql(busca))[0][0] 
                
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
            
                
            myworld.save()
        
    except:
            
        print("Falha de acesso!")
        
    del myworld, kiposcrum    
        
    contexto = {"lista_intancias": lista_intancias, "query_feita": query_feita, "quantidade_triplets": quantidade_triplets}
    
    return render(request, 'instancias.html', contexto)