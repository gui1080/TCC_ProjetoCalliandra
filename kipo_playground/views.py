from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm, inserir_instancias_tipoForm
from owlready2 import *         # https://pypi.org/project/Owlready2/
from os.path import exists
import numpy 

# source venv/bin/activate
# python3 manage.py runserver

# ------------------------------------------------------------

def faz_id(input_str):
    
    resultado_id = str(abs(hash(input_str)) % (10 ** 4))
    
    if len(resultado_id) == 3:
        
        resultado_id = "0" + resultado_id

    elif len(resultado_id) == 2:

        resultado_id = "00" + resultado_id
    
    elif len(resultado_id) == 1:
    
        resultado_id = "000" + resultado_id
    
    return resultado_id

# ------------------------------------------------------------
def welcome(request):
    
    return render(request, 'welcome.html')

# MÓDULO DE GESTÃO DE SPRINTS
# ------------------------------------------------------------

'''

def sprint_select(request):


def sprint_add(request):


def sprint_dashboard(request):

'''

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
    
        if 'num_inst' in request.session:
            del request.session['num_inst']
            
            
        if 'status' in request.session:
            del request.session['status']
            
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
        
        objetos_final = []
        
        try:
        
            with kiposcrum:
                
                lista_instancias = kiposcrum[input_dado].instances()
        
                num_inst = len(lista_instancias)
                
                status = "OK!"
                
                list_nomes = []
                list_obs = []
                
                for i in range(len(lista_instancias)):
                    
                    list_nomes.append(lista_instancias[i].Nome[0])
                
                    if not lista_instancias[i].Observacao:
                        list_obs.append("Sem observações")
                    else:
                        list_obs.append(lista_instancias[i].Observacao)
                
                
                for i in range(len(lista_instancias)):
                    objetos_final.append({'instancia':lista_instancias[i],'nome':list_nomes[i], 'obs':list_obs[i]})
                
                
                
                #print(lista_instancias)
        
                myworld.close() # só fecha o bd, deixa as instâncias no bd
                #myworld.save() # persiste na ontologia
        
        except:
            
            status = "Erro!" 
            num_inst = "Desconhecido"
            
            print("Falha de acesso!")
        
        #del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        #request.session['input_dado'] = lista_instancias
        request.session['num_inst'] = num_inst
        request.session['status'] = status
        
        context = {"objetos_final": objetos_final}
        return render(request, 'instancias_tipo_show.html', context)
    
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
        
        if 'nome' in request.session:
            del request.session['nome']
    
        if 'classe' in request.session:
            del request.session['classe']
            
        if 'observacao' in request.session:
            del request.session['observacao']
            
        input_nome = str(request.POST.get('nome'))
        input_classe = str(request.POST.get('classe'))
        input_observacao = str(request.POST.get('observacao'))
        
        status = "Indefinido"
        
        print(input_nome)
        print(input_classe)
        print(input_observacao)
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
        
        seed = str(time.time())
        id_unico = "000"
        
        try:
        
            with kiposcrum:
                
                '''
                kiposcrum["KIPCO__Agent"].instances()
                
                kiposcrum["KIPCO__Agent"]("desenvolvedornovo")!!

                kiposcrum.KIPCO__Agent("desenvolvedornovo")
                
                kiposcrum["desenvolvedor1"].is_a()
                '''
                
                kiposcrum[input_classe](input_nome + id_unico)
                
                if input_observacao != "":
                    kiposcrum[input_nome + id_unico].Observacao.append(input_observacao)
                
                sync_reasoner()
                
                status = "OK!"
                
                
                myworld.close() # só fecha o bd, deixa as instâncias no bd
                #myworld.save() # persiste na ontologia
        
        except:
            
            print("Falha de acesso!")
            status = "Erro!"
            input_nome = "Não foi recuperado"
            input_classe = "Não foi recuperado"
        
        #del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_nome'] = input_nome + id_unico
        request.session['input_classe'] = input_classe
        request.session['ontologia_status'] = status
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
            
            lista_instancias = kiposcrum["KIPCO__Agent"].instances() 
            print("foi")
            list_nomes = []
            list_obs = []
            objetos_final = []
            
            for i in range(len(lista_instancias)):
                
                list_nomes.append(lista_instancias[i].Nome[0])
                
                if not lista_instancias[i].Observacao:
                    list_obs.append("Sem observações")
                else:
                    list_obs.append(lista_instancias[i].Observacao)
            
            for i in range(len(lista_instancias)):
                objetos_final.append({'instancia':lista_instancias[i],'nome':list_nomes[i], 'obs':list_obs[i]})
                
            num_inst = len(lista_instancias)
            
            status = "OK!"
            
            myworld.close() # só fecha o bd, deixa as instâncias no bd
            #myworld.save() # persiste na ontologia
        
    except:
        
        lista_final = ["Erro!"]
        status = "Erro!"
        print("Falha de acesso!")
        num_inst = 0
        
    #del myworld, kiposcrum   
    
    #print(lista_final)
    
    contexto = {"objetos_final": objetos_final, "query_feita": query_feita, "num_inst": num_inst, "status": status}
    
    return render(request, 'instancias.html', contexto)