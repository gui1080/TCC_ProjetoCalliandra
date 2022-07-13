from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm
from owlready2 import *         # https://pypi.org/project/Owlready2/

# source venv/bin/activate
# python3 manage.py runserver

# Create your views here.

def welcome(request):
    
    return render(request, 'welcome.html')

def instancias_tipo_show(request):
    
    return render(request, 'instancias_tipo_show.html',)

def instancias_tipo(request):
    
    form = novo_instancias_tipoForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'input_dado' in request.session:
            del request.session['input_dado']
    
        input_dado = request.POST.get('busca')
        
        print(input_dado)
        
        # OWLREADY2
        
        myworld = World(filename='kiposcrum_backup.db', exclusive=False)
        
        onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum.owl').load()
        
        try:
        
            with kiposcrum:
                
                busca = """
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX scrum: <http://www.semanticweb.org/guilhermebraga/ontologies/2022/5/kiposcrum#>
                    SELECT ?y
                    {   
                        ?x rdfs:label scrum:scrumRoles .
                        ?y a/rdfs:subClassOf* ?x 
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
        request.session['input_dado'] = "resultado_query"
        return redirect('/kipo_playground/instancias_tipo_show/')
    
    return render(request, 'instancias_tipo_select.html', context)

def instancias_teste(request):
        
    myworld = World(filename='kiposcrum_backup.db', exclusive=False)
        
    onto_path.append(os.path.dirname(__file__))
        
    # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
    kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum.owl').load()
    
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
        
    contexto = {"lista_intancias": lista_intancias, "query_feita": query_feita}
    
    return render(request, 'instancias.html', contexto)