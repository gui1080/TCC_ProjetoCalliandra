from multiprocessing import context
from typing import final
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm, inserir_instancias_tipoForm, inserir_instancias_sprintForm
from owlready2 import *         # https://pypi.org/project/Owlready2/
from os.path import exists
import json 
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
    
    if 'status' in request.session:
        del request.session['status']
    
    # pegar quantidade de scrum_Sprint
    # quantidade de KIPCO__Agent
    # quantidade de Task_Description
    # quantidade de scrum_Daily
    # quantidade de DO__Decision
    ''' Formato dos dados pro Gráfico de Barras
    [['Year', 'Sales'],
    ['2014', 1000],
    ['2015', 1170],
    ['2016', 660],
    ['2017', 1030] ]
    '''
    
    
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
    except:
            
        print("Erro no começo")
        
    sync_reasoner()
    
    #-----------------------------------------------------
    
    lista_dados_qtd_fim = []
    
    try:
        
        with kiposcrum:
            
            
            status = "OK!"
            
            qtd_agentes = len(kiposcrum["KIPCO__Agent"].instances())
            qtd_taskdescription = len(kiposcrum["Task_Description"].instances())
            qtd_daily = len(kiposcrum["scrum_Daily"].instances())
            qtd_decision = len(kiposcrum["DO__Decision"].instances())
            
            lista_dados_qtd = [["Classe", "Quantidade"],
                                ["KIPCO__Agent", qtd_agentes], 
                                ["Task_Description", qtd_taskdescription], 
                                ["scrum_Daily", qtd_daily], 
                                ["DO__Decision", qtd_decision]]
            
            lista_dados_qtd_fim = json.dumps(lista_dados_qtd)
            
            myworld.close()
            
    except:
        
        qtd_agentes = 0
        status = "Erro!"
    
    context = {"lista_dados_qtd": lista_dados_qtd_fim}
    request.session['status'] = status
    return render(request, 'welcome_graficos.html', context)

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

# !SELECIONA DECISAO
# !------------------------------------------------------------

def decision_select(request):
    
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
                
            lista_instancias = kiposcrum["DO__Decision"].instances()
            
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
    return render(request, 'seleciona_decisao.html', context)
    
# VER DADOS DA DECISAO
def decision_dashboard(request, instancia_decisao):
    
    # instancia_decisao é a decisao a ser usada
    
    
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
            
            print("Criando dashboard de DO__Decision!")
            
            num_inst = 0
            
            # a query sai com prefixo "kipo."
            instancia = instancia_decisao[5:]
            print(instancia)
            
            # propriedades
            propriedades = kiposcrum[instancia].get_properties()
            print(propriedades)
            num_prop_correlatas = len(propriedades)
            
            
            '''
            propriedades!
            
            {kipo.StatusProblemaResolvido, kipo.INV_influences, kipo.INV_composes, 
            kipo.INV_ontoscrum__performs, kipo.pos_state, 
            kipo.considers, kipo.Nome, kipo.INV_threatens}

            
            '''
            
            # decisão influenciada por
            INV_influences = kiposcrum[instancia].INV_influences
            print("INV_influences " + str(INV_influences))
            num_inst = num_inst + len(INV_influences)
            
            # itens que compoem decisão
            INV_composes = kiposcrum[instancia].INV_composes
            print("INV_composes " + str(INV_composes))
            num_inst = num_inst + len(INV_composes)
            
            # decisao considera
            considers = kiposcrum[instancia].considers
            print("considers " + str(considers))
            num_inst = num_inst + len(considers)
            
            # decisao ameaçada por
            INV_threatens = kiposcrum[instancia].INV_threatens
            print("INV_threatens " + str(INV_threatens))
            num_inst = num_inst + len(INV_threatens)
            
            objeto_INV_influences = transforma_objeto(INV_influences)
            objeto_INV_composes = transforma_objeto(INV_composes)
            objeto_considers = transforma_objeto(considers)
            objeto_INV_threatens = transforma_objeto(INV_threatens)
            
            
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
    
    context = {"instancia_decision": instancia_decisao, "objeto_INV_influences": objeto_INV_influences, "objeto_INV_composes": objeto_INV_composes, "objeto_considers": objeto_considers, "objeto_INV_threatens": objeto_INV_threatens}
    
    return render(request, 'decision_dashboard.html', context)
    
    

    
    
def transforma_objeto(lista_instancias):
    
    objetos_final = []
    
    list_nomes = []
    list_obs = []
    list_classe = []
    
    if len(lista_instancias) == 0:
        
        list_nomes.append("Sem Nome!")
        list_classe.append("Sem Classe!")
        list_obs.append("Sem Observações!")
        lista_instancias.append("Sem instancias!")
        
        objetos_final.append({'classe_inst': "Sem Classe!", 'instancia': "Sem instancias!",'nome': "Sem Nome!", 'obs': "Sem Observações!"})

        
    else:
    
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
        
        if 'input_dado' in request.session:
            del request.session['input_dado']
    
        input_nome = request.POST.get('nome')
        input_classe = request.POST.get('classe')
        input_obs = request.POST.get('observacao')
        
        print(input_nome)
        print(input_classe)
        
        
        # OWLREADY2
        
        myworld = World(filename='backup.db', exclusive=False)
        
        onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
        
        
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
                
                myworld.sparql(busca)

                # Sincronização
                #--------------------------------------------------------------------------
                
                print("\n------------------------------------\n")
                print("Sincronização!")
                
                
                sync_reasoner()
                
                status = "OK!"
                myworld.save()
        
        except:
            
            status = "Erro!"
            print("Falha de acesso!")
        
        myworld.close()
        
        del myworld, kiposcrum    
        
        # fazer uma query aqui de SPARQL
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_nome'] = input_nome
        request.session['input_classe'] = input_classe
        request.session['input_status'] = status
        return redirect('/kipo_playground/inserir_instancia_tela_ok/')
        
    
    return render(request, 'instancias_inserir_select.html', context)



# ------------------------------------------------------------

'''

    
def daily_add(request):
    

'''

def ver_sprint_backlog(request, instancia_sprint):
    
    if 'num_inst' in request.session:
        del request.session['num_inst']
            
    if 'status' in request.session:
        del request.session['status']
        
    if 'num_prop_correlatas' in request.session:
        del request.session['num_prop_correlatas']
        
        
    instancia = instancia_sprint[5:]
    print(instancia)
    
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
    
    status = "OK!" 
    
    try:
        
        with kiposcrum:
            
            print("Criando Visualização de Sprint Backlog!")
            
            instancia_backlog_sprint = str(kiposcrum[instancia].ontoscrum__has_input.pop(0))
            
            backlog_sprint = instancia_backlog_sprint[5:]
            
            print(backlog_sprint)
            
            propriedades = kiposcrum[backlog_sprint].get_properties()
            print(propriedades)
            num_prop_correlatas = len(propriedades)
            
            num_inst = 0
            
            # faz as queries do que vai para a tela!
            '''
            {kipo.ontoscrum__during, kipo.ontoscrum__has_input, kipo.Nome, 
            kipo.ontoscrum__contains, kipo.ontoscrum__has_output, kipo.ontoscrum__is_executed_by, 
            kipo.ontoscrum__is_managed_by, kipo.INV_ontoscrum__affects, kipo.INV_ontoscrum__has_input, 
            kipo.ontoscrum__performs, kipo.INV_ontoscrum__has_output}
            '''
            
            # sprint backlog contains task descriptions!
            contains = kiposcrum[backlog_sprint].ontoscrum__contains
            print("Contains" + str(contains))
            num_inst = num_inst + len(contains)
            
            # o que ocorre durante essa sprint?
            during = kiposcrum[backlog_sprint].ontoscrum__during
            print("During" + str(during))
            num_inst = num_inst + len(during)
            
            # input
            has_input = kiposcrum[backlog_sprint].ontoscrum__has_input
            print("has_input" + str(has_input))
            num_inst = num_inst + len(has_input)
            
            # output
            has_output = kiposcrum[backlog_sprint].ontoscrum__has_output
            print("has_output" + str(has_output))
            num_inst = num_inst + len(has_output)
            
            # sprint performs o que?
            performs = kiposcrum[backlog_sprint].ontoscrum__performs
            print("performs" + str(performs))
            num_inst = num_inst + len(performs)
            
            # quem executa sprint?
            is_executed_by = kiposcrum[backlog_sprint].ontoscrum__is_executed_by
            print("is_executed_by" + str(is_executed_by))
            num_inst = num_inst + len(is_executed_by)
            
            
            objeto_contains = transforma_objeto(contains)
            objeto_during = transforma_objeto(during)
            objeto_has_input = transforma_objeto(has_input)
            objeto_has_output = transforma_objeto(has_output)
            objeto_performs = transforma_objeto(performs)
            objeto_is_executed_by = transforma_objeto(is_executed_by)
            
            myworld.close()
    except:
        
        status = "Erro!" 
        num_prop_correlatas = "Desconhecido"
        num_inst = "?"
        instancia = "Erro!" 
        
        print("Falha de acesso!")
    
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    #context = {"instancia_backlog": instancia_backlog, "objeto_ismanagedby": objeto_ismanagedby, "objeto_contains": objeto_contains}
    
    context = {"instancia_backlog_sprint":instancia_backlog_sprint, "objeto_contains": objeto_contains, "objeto_during": objeto_during, "objeto_has_input": objeto_has_input, "objeto_has_output": objeto_has_output, "objeto_performs": objeto_performs, "objeto_is_executed_by": objeto_is_executed_by}
    
    return render(request, 'backlog_sprint.html', context)


def ver_backlog_produto(request):
    
    # ObjectProperty!
    # ontoscrum__originator
    # ontoscrum__is_managed_by
    # ontoscrum__contains -> um item que ontoscrum__contains features e releaseplan
    
    # DataProperty!
    # EstimatedBusinessValue
    
    
    if 'num_inst' in request.session:
        del request.session['num_inst']
            
    if 'status' in request.session:
        del request.session['status']
        
    if 'num_prop_correlatas' in request.session:
        del request.session['num_prop_correlatas']
    
  
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
            
            # falta o ontoscrum__originator
            # {kipo.Nome, kipo.ontoscrum__originator, kipo.ontoscrum__is_managed_by, kipo.INV_ontoscrum__has_output, 
            # kipo.INV_ontoscrum__has_input, kipo.INV_uses, kipo.INV_ontoscrum__affects, 
            # kipo.ontoscrum__contains, kipo.contains}
            
            print("Criando Visualização de Product Backlog!")
            
            num_inst = 0
            
            # kiposcrum.KIPCO__Agent("desenvolvedornovo")
            
            # add kipo.backlog_sistema_venda_livros9221 contains do_decision na main de testes
            
            instancia_backlog = str(kiposcrum["Product_Backlog"].instances().pop(1))
            
            print(instancia_backlog)
            
            print(kiposcrum["Product_Backlog"].instances())
            instancia = instancia_backlog[5:]
            #print(instancia)
            
            status = "OK!" 
            
            # propriedades
            propriedades = kiposcrum[instancia].get_properties()
            print(propriedades)
            num_prop_correlatas = len(propriedades)
            
            # lista de instâncias tudo que ocorre ontoscrum__during
            #originator = kiposcrum[instancia].ontoscrum__originator
            #print("Originator " + str(originator))
            #num_inst = num_inst + len(originator)
            
            ismanagedby = kiposcrum[instancia].ontoscrum__is_managed_by
            print("Ismanagedby" + str(ismanagedby))
            num_inst = num_inst + len(ismanagedby)
            
            contains = kiposcrum[instancia].ontoscrum__contains
            print("Contains" + str(contains))
            num_inst = num_inst + len(contains)
            
            # objeto_originator = transforma_objeto(originator)
            objeto_ismanagedby = transforma_objeto(ismanagedby)
            objeto_contains = transforma_objeto(contains)    # pegar estimated business values
            
            # se no objeto contains a classe é Decisão, fazer botão do dashboard
            # da pra fazer isso no html
            
            # pegar objeto de contains com EstimatedBusinessValue
            #------------------------------
            '''
            objeto_contains = []
            
            list_nomes = []
            list_obs = []
            list_classe = []
            list_estimated_value = []
            
            for i in range(len(contains)):
                
                # esse jeito de recuperar data property tá errado
                list_estimated_value.append(str(kiposcrum[instancia].EstimatedBusinessValue))
                
                list_nomes.append(str(contains[i].Nome[0]))
                        
                list_classe.append(str(contains[i].is_a.pop(0)))
                        
                if not contains[i].Observacao:
                    list_obs.append("Sem observações")
                else:
                    list_obs.append(str(contains[i].Observacao))
                    
                print("---------------")
                print(len(list_nomes))
                print(len(list_obs))
                print(len(list_classe))
                print(len(contains))
                print("current estimated business value " + str(kiposcrum[instancia].EstimatedBusinessValue))
                print("estimated business values " + str(list_estimated_value.pop(0)))
                print(str(contains[0]))
                print("---------------")
            
            # 'estimatedbusinessvalue': list_estimated_value[i]    
            for i in range(len(contains)):
                objeto_contains.append({'classe_inst':list_classe[i], 'instancia':str(contains[i]),'nome':list_nomes[i], 'obs':list_obs[i] })
                    
                    
            #------------------------------
            '''
            
            
            myworld.close() 
        
    except:
            
        status = "Erro!" 
        num_prop_correlatas = "Desconhecido"
        num_inst = "?"
        instancia_backlog = "Erro!"
        instancia = "Erro!" 
        
        print("Falha de acesso!")
    
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia_backlog": instancia_backlog, "objeto_ismanagedby": objeto_ismanagedby, "objeto_contains": objeto_contains}
    
    return render(request, 'backlog_produto.html', context)

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
        
        context = {"objetos_final": objetos_final, "query_feita": query_feita, "num_inst": num_inst, "status": status}
    
    return render(request, 'instancias.html', context)