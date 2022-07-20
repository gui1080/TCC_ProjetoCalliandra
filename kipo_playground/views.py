from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm, inserir_instancias_tipoForm
from owlready2 import *         # https://pypi.org/project/Owlready2/
from os.path import exists

# source venv/bin/activate
# python3 manage.py runserver

# ------------------------------------------------------------
def welcome(request):
    
    return render(request, 'welcome.html')
# ------------------------------------------------------------


# DESSA FORMA É POSSÍVEL VER TODAS AS INSTÂNCIAS DE UMA CLASSE
# instancias_tipo -> instancias_tipo_show
# ------------------------------------------------------------

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
    
        input_dado = str(request.POST.get('busca'))
        
        print(input_dado)
        
        # OWLREADY2
        try:
            
            myworld = World(filename='backup.db', exclusive=False)
            
            #onto_path.append(os.path.dirname(__file__))
            
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
        except:
        
            print("Erro no começo")
        
        sync_reasoner()
        
        try:
        
            with kiposcrum:
                
                '''
                
                
                kiposcrum["KIPCO__Agent"].instances()
                
                kiposcrum["KIPCO__Agent"]("desenvolvedornovo")!!

                kiposcrum.KIPCO__Agent("desenvolvedornovo")
                
                kiposcrum["desenvolvedor1"].is_a()
                
                
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
                    
                lista_instancias = list(myworld.sparql(busca)) 
                
                '''
            
                lista_instancias = str(kiposcrum[input_dado].instances())
            
                print(lista_instancias)
        
                myworld.close() # só fecha o bd, deixa as instâncias no bd
                #myworld.save() # persiste na ontologia
        
        except:
            
            lista_instancias = "Erro!"
            
            print("Falha de acesso!")
        
        #del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_dado'] = lista_instancias
        return redirect('/kipo_playground/instancias_tipo_show/')
    
    return render(request, 'instancias_tipo_select.html', context)

# INSERINDO INSTÂNCIAS
# inserir_instancia -> inserir_instancia_tela_ok
# ------------------------------------------------------------

def inserir_instancia_tela_ok(request):
    # menu de mostrar instancia pra botar + espaço pra definir o nome
    return render(request, 'inserir_instancia_tela_ok.html')

# instancia pra botar + espaço pra definir o nome
def inserir_instancia(request):

    form = inserir_instancias_tipoForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'input_dado' in request.session:
            del request.session['input_dado']
    
        input_nome = str(request.POST.get('nome'))
        input_classe = str(request.POST.get('classe'))
        status = "Indefinido"
        
        print(input_nome)
        print(input_classe)
        print(status)
        
        
        # OWLREADY2
        try:
            
            myworld = World(filename='backup.db', exclusive=False)
            
            #onto_path.append(os.path.dirname(__file__))
            
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
        except:
            
            print("Erro no começo")
            
        
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
        
        
        try:
        
            with kiposcrum:
                
                '''
                kiposcrum["KIPCO__Agent"].instances()
                
                kiposcrum["KIPCO__Agent"]("desenvolvedornovo")!!

                kiposcrum.KIPCO__Agent("desenvolvedornovo")
                
                kiposcrum["desenvolvedor1"].is_a()
                '''
                
                kiposcrum[input_classe](input_nome)
                
                sync_reasoner()
                
                if str(kiposcrum[input_nome]) == None:
                    
                    status = "Erro"
                
                else:
                    
                    status = "OK!"
                
                
                myworld.close() # só fecha o bd, deixa as instâncias no bd
                #myworld.save() # persiste na ontologia
        
        except:
            
            print("Falha de acesso!")
        
        #del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_nome'] = input_nome
        request.session['input_classe'] = input_classe
        request.session['input_status'] = status
        return redirect('/kipo_playground/inserir_instancia_tela_ok/')
        
    
    return render(request, 'instancias_inserir_select.html', context)

# TESTE DE ACESSO AO BANCO DE DADOS
# ------------------------------------------------------------

def instancias_teste(request):
    
    # OWLREADY2
    try:
        
        myworld = World(filename='backup.db', exclusive=False)
        
        #onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
        
    except:
        
        print("Erro no começo")
        
    query_feita = "kiposcrum['KIPCO__Agent'].instances()"
    
    print(query_feita)
    
    sync_reasoner()
    
    # se não for nessa estrutura, dá TABLE LOCKED!
    try:
        
        with kiposcrum:
            
            lista_instancias = str( kiposcrum["KIPCO__Agent"].instances() )
            
            #print(lista_instancias)
            
            myworld.close() # só fecha o bd, deixa as instâncias no bd
            #myworld.save() # persiste na ontologia
        
    except:
        
        lista_instancias = ["Erro!"]
        print("Falha de acesso!")
        
    #del myworld, kiposcrum   
    
    print(lista_instancias) 
        
    contexto = {"lista_instancias": lista_instancias, "query_feita": query_feita}
    
    return render(request, 'instancias.html', contexto)