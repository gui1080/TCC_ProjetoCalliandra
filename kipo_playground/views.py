from multiprocessing import context
from typing import final
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm, inserir_instancias_tipoForm, inserir_instancias_sprintForm
from owlready2 import *         # https://pypi.org/project/Owlready2/
from os.path import exists
import numpy 
import sys

# Comandos básicos
# source venv/bin/activate
# python3 manage.py runserver

# !SCRIPTS AUXILIARES
# !------------------------------------------------------------
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

# ------------------------------------------------------------
def sobre(request):
    
    return render(request, 'sobre.html')

# !MÓDULO DE GESTÃO DE SPRINTS


# !SELECIONA SPRINT
# !------------------------------------------------------------

def sprint_select(request):
    
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
    except:
            
        print("Erro no começo")
        
    sync_reasoner()
        
    objetos_final = []
        
    try:
        
        with kiposcrum:
                
            lista_instancias = kiposcrum["scrum_Sprint"].instances()
            
            print("\n\n\n\n")
            print(lista_instancias)
            print("\n\n\n\n")
            
            num_inst = len(lista_instancias)
            
            print("\n\n\n\n")
            print(num_inst)
            print("\n\n\n\n")
                
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
                
            myworld.close() # só fecha o bd, deixa as instâncias no bd
            
    except:
            
        status = "Erro!" 
        num_inst = "Desconhecido"
        
        print("---------------------------")
        print("Falha de acesso!")
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        
        print("---------------------------")

    
    
    
    request.session['num_inst'] = num_inst
    request.session['status'] = status
        
    context = {"objetos_final": objetos_final}
    return render(request, 'seleciona_sprint.html', context)
    
def transforma_objeto(lista_instancias):
    
    objetos_final = []
    
    list_nomes = []
    list_obs = []
    list_classe = []
                
    for i in range(len(lista_instancias)):
                    
        list_nomes.append(str(lista_instancias[i].Nome[0]))
        
        list_classe.append(str(lista_instancias[i].is_a.pop(0)))
        
        if not lista_instancias[i].Observacao:
            list_obs.append("Sem observações")
        else:
            list_obs.append(str(lista_instancias[i].Observacao))
    
    print("---------------")
    print(len(list_nomes))
    print(len(list_obs))
    print(len(list_classe))
    print(len(lista_instancias))
    print(str(lista_instancias[0]))
    print("---------------")
    
    for i in range(len(lista_instancias)):
        objetos_final.append({'classe_inst':list_classe[i], 'instancia':str(lista_instancias[i]),'nome':list_nomes[i], 'obs':list_obs[i]})
    
    return objetos_final                 

# !SPRINT
#!-----------------------------------------------------

# VER DADOS DA SPRINT
def sprint_dashboard(request, instancia_sprint):
    
    # instancia_sprint é a sprint a ser usada
    
    
    if 'num_inst' in request.session:
        del request.session['num_inst']
            
    if 'status' in request.session:
        del request.session['status']
        
    if 'num_prop_correlatas' in request.session:
        del request.session['num_prop_correlatas']
        
    if 'num_inst' in request.session:
        del request.session['num_inst']
        
        
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        #onto_path.append(os.path.dirname(__file__))
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
    except:
        
        print("Erro no começo")
        
    sync_reasoner()
    
    #-----------------------------------------------------
    
    try:
        
        with kiposcrum:
            
            print("Criando dashboard de Sprint!")
            
            num_inst = 0
            
            # kiposcrum.KIPCO__Agent("desenvolvedornovo")
            
            # a query sai com prefixo "kipo."
            instancia = instancia_sprint[5:]
            print(instancia)
            
            # propriedades
            propriedades = kiposcrum[instancia].get_properties()
            print(propriedades)
            num_prop_correlatas = len(propriedades)
            
            # lista de instâncias tudo que ocorre ontoscrum__during
            during = kiposcrum[instancia].ontoscrum__during
            print("During " + str(during))
            num_inst = num_inst + len(during)
            
            # lista de instâncias tudo que ocorre ontoscrum__has_input
            has_input = kiposcrum[instancia].ontoscrum__has_input
            print("Input " + str(has_input))
            num_inst = num_inst + len(has_input)

            # lista de instâncias tudo que ocorre ontoscrum__has_has_output
            has_output = kiposcrum[instancia].ontoscrum__has_output
            print("Output " + str(has_output))
            num_inst = num_inst + len(has_output)
    
            # lista de instâncias tudo que ocorre ontoscrum__isExecutedBy
            has_isexecutedby = kiposcrum[instancia].ontoscrum__is_executed_by
            print("Executado por " + str(has_isexecutedby))
            num_inst = num_inst + len(has_isexecutedby)

            # lista de instâncias tudo que ocorre ontoscrum__simultaneously
            INV_simultaneo = kiposcrum[instancia].INV_ontoscrum__simultaneously
            print("Simultaneo " + str(INV_simultaneo))
            num_inst = num_inst + len(INV_simultaneo)
            
            objeto_during = transforma_objeto(during)
            objeto_has_input = transforma_objeto(has_input)
            objeto_has_output = transforma_objeto(has_output)
            objeto_has_isexecutedby = transforma_objeto(has_isexecutedby)
            objeto_INV_simultaneo = transforma_objeto(INV_simultaneo)
            
            status = "OK!" 
            myworld.close() 
        
    except:
            
        status = "Erro!" 
        num_inst = "Desconhecido"
        num_prop_correlatas = "Desconhecido"
        num_inst = 0
            
        print("Falha de acesso!")
    
    request.session['num_inst'] = num_inst
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia_sprint":instancia_sprint , "objetos_during":objeto_during, "objetos_has_input":objeto_has_input, "objetos_has_output":objeto_has_output,
                "objetos_has_isexecutedby":objeto_has_isexecutedby, "objetos_INV_simultaneo":objeto_INV_simultaneo}
    
    return render(request, 'sprint_dashboard.html', context)
    
    

def sprint_add(request):

    form = inserir_instancias_sprintForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'nome' in request.session:
            del request.session['nome']
        if 'observacao' in request.session:
            del request.session['observacao']
            
        input_nome = str(request.POST.get('nome'))
        input_classe = "scrum_Sprint"
        input_observacao = str(request.POST.get('observacao'))
        
        status = "Erro!"
        
        # OWLREADY2
        try:
            
            myworld = World(filename='backup.db', exclusive=False)
            
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
        except:
        
            print("Erro no começo")
        
        sync_reasoner()
        
        seed = str(time.time())
        id_unico = faz_id(seed)
        
        try:
        
            with kiposcrum:
                
                kiposcrum[input_classe](input_nome + id_unico)
                
                if input_observacao != "":
                    kiposcrum[input_nome + id_unico].Observacao.append(input_observacao)
                
                sync_reasoner()
                
                status = "OK!"
                
                
                myworld.save() # persiste na ontologia
                myworld.close()
        
        except:
            
            print("Falha de acesso!")
            input_nome = "Não foi recuperado"
            input_classe = "Não foi recuperado"
        
        finally:
            
            # faz query e bota resultado na sessão, um redirect vai botar o resultado
            request.session['input_nome'] = input_nome + id_unico
            request.session['input_classe'] = input_classe
            request.session['ontologia_status'] = status
            return redirect('/kipo_playground/inserir_instancia_tela_ok/')
            
        
        
    
    return render(request, 'instancias_tipo_select.html', context)

# ------------------------------------------------------------

# !VISUALIZAÇÃO DE TRABALHO DIÁRIO DENTRO DE UMA SPRINT
# !------------------------------------------------------------

def daily_dashboard(request, instancia_daily):
    
    
    # a query sai com prefixo "kipo."
    instancia = instancia_daily[5:]
    print(instancia)
    
    context = {"instancia_daily":instancia_daily}
    
    
    # ontoscrum__perfoms
    # INV_ontoscrum__during
    # ontoscrum__hasOutput
    # ontoscrum__hasInput
    # ontoscrum__is_executed_by
    
    # instancia_sprint é a sprint a ser usada
    
    
    if 'num_inst' in request.session:
        del request.session['num_inst']
            
    if 'status' in request.session:
        del request.session['status']
        
    if 'num_prop_correlatas' in request.session:
        del request.session['num_prop_correlatas']
        
    if 'num_inst' in request.session:
        del request.session['num_inst']
        
        
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        #onto_path.append(os.path.dirname(__file__))
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
    except:
        
        print("Erro no começo")
        
    sync_reasoner()
    
    #-----------------------------------------------------
    
    try:
        
        with kiposcrum:
            
            print("Criando dashboard de Sprint!")
            
            num_inst = 0
            
            # kiposcrum.KIPCO__Agent("desenvolvedornovo")
            
            # a query sai com prefixo "kipo."
            instancia = instancia_daily[5:]
            print(instancia)
            
            # propriedades
            propriedades = kiposcrum[instancia].get_properties()
            print(propriedades)
            num_prop_correlatas = len(propriedades)
            
            # lista de instâncias tudo que ocorre ontoscrum__during
            inv_during = kiposcrum[instancia].INV_ontoscrum__during
            print("INV_During " + str(inv_during))
            num_inst = num_inst + len(inv_during)
            
            # lista de instâncias tudo que ocorre ontoscrum__has_input
            has_input = kiposcrum[instancia].ontoscrum__has_input
            print("Input " + str(has_input))
            num_inst = num_inst + len(has_input)

            # lista de instâncias tudo que ocorre ontoscrum__has_has_output
            has_output = kiposcrum[instancia].ontoscrum__has_output
            print("Output " + str(has_output))
            num_inst = num_inst + len(has_output)
    
            # lista de instâncias tudo que ocorre ontoscrum__isExecutedBy
            has_isexecutedby = kiposcrum[instancia].ontoscrum__is_executed_by
            print("Executado por " + str(has_isexecutedby))
            num_inst = num_inst + len(has_isexecutedby)

            # lista de instâncias tudo que ocorre ontoscrum__simultaneously
            performs = kiposcrum[instancia].ontoscrum__performs
            print("Performs " + str(performs))
            num_inst = num_inst + len(performs)
            
            objeto_inv_during = transforma_objeto(inv_during)
            objeto_has_input = transforma_objeto(has_input)
            objeto_has_output = transforma_objeto(has_output)
            objeto_has_isexecutedby = transforma_objeto(has_isexecutedby)
            objeto_performs = transforma_objeto(performs)
            
            status = "OK!" 
            myworld.close() 
        
    except:
            
        status = "Erro!" 
        num_prop_correlatas = "Desconhecido"
        num_inst = "?"
            
        print("Falha de acesso!")
    
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia":instancia_daily , "objeto_inv_during":objeto_inv_during, "objetos_has_input":objeto_has_input, "objetos_has_output":objeto_has_output,
                "objetos_has_isexecutedby":objeto_has_isexecutedby, "objeto_performs":objeto_performs}
    
    
    return render(request, 'daily_dashboard.html', context)
    

# ------------------------------------------------------------

# !VISUALIZAÇÃO DE INSTÂNCIAS DE UMA CLASSE
# !------------------------------------------------------------


# instancias_tipo -> instancias_tipo_show

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

# !INSERINDO INSTÂNCIAS
# !------------------------------------------------------------

# inserir_instancia -> inserir_instancia_tela_ok

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
        id_unico = faz_id(seed)
        
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
                myworld.save() # persiste na ontologia
        
        except:
            
            print("Falha de acesso!")
            status = "Erro!"
            input_nome = "Não foi recuperado"
            input_classe = "Não foi recuperado"
        
        finally:
            
            #del myworld, kiposcrum    
            
            # fazer uma query aqui de SPARQL
            
            # faz query e bota resultado na sessão, um redirect vai botar o resultado
            request.session['input_nome'] = input_nome + id_unico
            request.session['input_classe'] = input_classe
            request.session['ontologia_status'] = status
            
            print("\n\n\n\n\n")
            print(status)
            print("\n\n\n\n\n")
            
            return redirect('/kipo_playground/inserir_instancia_tela_ok/')
            
    
    return render(request, 'instancias_inserir_select.html', context)

# ------------------------------------------------------------

'''

def ver_sprint_backlog(request, instancia_sprint):
    
    
def daily_add(request):
    

'''

def ver_backlog_produto(request):
    
    # ObjectProperty!
    # ontoscrum__originator
    # ontoscrum__is_managed_by
    # ontoscrum__contains -> um item que ontoscrum__contains features e releaseplan
    
    # DataProperty!
    # EstimatedBusinessValue
    
    return render(request, 'backlog_produto.html')

# !TESTE DE ACESSO AO BANCO DE DADOS
# !------------------------------------------------------------

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
    
    list_nomes = []
    list_obs = []
    objetos_final = []
    # se não for nessa estrutura, dá TABLE LOCKED!
    try:
        
        with kiposcrum:
            
            lista_instancias = kiposcrum["KIPCO__Agent"].instances() 
            print("foi")
            
            
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
        
    finally:
        
        contexto = {"objetos_final": objetos_final, "query_feita": query_feita, "num_inst": num_inst, "status": status}
    
    return render(request, 'instancias.html', contexto)