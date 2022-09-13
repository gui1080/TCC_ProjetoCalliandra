"""Módulo de Views de kipo_playground

Módulo principal que define a visualização com contexto de templates em HTML na pasta '/kipo_playground/templates', que também usa '/kipo_playground/static'.

Módulo de gestão de formulários, gestão de Banco de Dados e definição de contexto por meio de acesso para ontologia '/kipo_playground/kipo_fialho.owl', com instâncias de caso de estudo definidas em 'backup.db'. 

Essas views são geridas com endereços por meio do arquivo 'urls.py'. 

"""

from multiprocessing import context
from typing import final
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import novo_instancias_tipoForm, inserir_instancias_tipoForm, inserir_instancias_dada_classeForm
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
    """ Pega uma string e gera um id único básico para cada instância na Ontologia.
        
        :param input_str: String que vai servir como input para o ID. 
    
        :return: Valor numérico único como string de até 4 caracteres. 
    """
    
    resultado_id = str(abs(hash(input_str)) % (10 ** 4))
    
    if len(resultado_id) == 3:
        
        resultado_id = "0" + resultado_id

    elif len(resultado_id) == 2:

        resultado_id = "00" + resultado_id
    
    elif len(resultado_id) == 1:
    
        resultado_id = "000" + resultado_id
    
    return resultado_id

    
def transforma_objeto(lista_instancias):
    """ Pega um objeto da Ontologia e transforma em um dicionário, no formato que o DJango bota no template corretamente.
        
        :param input_str: Lista de instâncias que viram objeto. 
    
        :return: Dicionário com campos 'classe', 'instância', 'nome' e 'observação'. 
    """
    
    objetos_final = []
    
    list_nomes = []
    list_obs = []
    list_classe = []
    
    if len(lista_instancias) == 0:
        
        list_nomes.append("Sem Nome!")
        list_classe.append("Sem Classe!")
        list_obs.append("Sem Observações!")
        #lista_instancias.append("Sem instancias!")
        
        objetos_final.append({'classe_inst': "Sem Classe!", 'instancia': "Sem instancias!",'nome': "Sem Nome!", 'obs': "Sem Observações!"})
        return objetos_final
        
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

# !------------------------------------------------------------

def welcome(request):
    """ View de tela de início do sistema.
        
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'welcome_graficos.html'. 
    """
    
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
    
    files = os.listdir('.')
    achou_bd = 0
    
    for file in files:
            
        if "backup.db" in file:
            achou_bd = 1
        
    if achou_bd == 0:
        print("NÃO ACHEI BD")
    
        
        # OWLREADY2
        try:
                
            myworld = World(filename='backup.db', exclusive=False)
            
            onto_path.append(os.path.dirname(__file__))
            
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
            
            kiposcrum["Product_Backlog"]("backlog_do_sistema" + "1234")
            kiposcrum["backlog_do_sistema" + "1234"].Nome.append("backlog_do_sistema")
            kiposcrum["backlog_do_sistema" + "1234"].Observacao.append("Criado automaticamente na abertura do sistema!")
        
            myworld.save()
        
        except:
            
            print("Erro no começo criando BD")
            
        finally:
            
            myworld.close()
            
            return render(request, 'welcome_graficos.html', context)
    
    
    else:    
    #-----------------------------------------------------
        
        
        lista_dados_qtd_fim = []
        
        try:
            
            myworld = World(filename='backup.db', exclusive=False)
            
            kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
            
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
                
                
                
        except:
            
            qtd_agentes = 0
            status = "Erro!"
        
        finally:
            myworld.close()
        
        context = {"lista_dados_qtd": lista_dados_qtd_fim}
        request.session['status'] = status
        return render(request, 'welcome_graficos.html', context)

def sobre(request):
    
    return render(request, 'sobre.html')

# !TESTE DE ACESSO AO BANCO DE DADOS
# !------------------------------------------------------------

def instancias_teste(request):
    """ View de tela de testes de acesso ao Banco de Dados. Visualização de Agentes.
        
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'instancias.html'. 
    """
    
    query_feita = "kiposcrum['KIPCO__Agent'].instances()"
    
    print(query_feita)
    
    sync_reasoner()
    
    list_nomes = []
    list_obs = []
    objetos_final = []


    # OWLREADY2
    try:
        
        myworld = World(filename='backup.db', exclusive=False)
        
        #onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
        
        with kiposcrum:
            
            lista_instancias = kiposcrum["KIPCO__Agent"].instances() 
            
            
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
            
        
    except:
        
        lista_final = ["Erro!"]
        status = "Erro!"
        print("Falha de acesso!")
        num_inst = 0
        
    finally:
        
        myworld.close()
        
        context = {"objetos_final": objetos_final, "query_feita": query_feita, "num_inst": num_inst, "status": status}
    
    return render(request, 'instancias.html', context)

# !VISUALIZAÇÃO DE INSTÂNCIAS DE UMA CLASSE
# !------------------------------------------------------------

# instancias_tipo -> instancias_tipo_show

# mostra o input de todas as instâncias de dada classe
def instancias_tipo_show(request):
    """ View de visualização de instâncias de uma dada classe no Banco de Dados. 
        
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'instancias_tipo_show.html'. 
    """
    
    return render(request, 'instancias_tipo_show.html')

# seleciona classe para ver
def instancias_tipo(request):
    """ View de seleção para visualização de instâncias de uma dada classe no Banco de Dados. 
        
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'instancias_tipo_show.html' (método POST) e instancias_tipo_select.html (método GET). 
    """
    
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
        
        objetos_final = []
        
        list_nomes = []
        list_obs = []
        
        # OWLREADY2
        try:
            
            myworld = World(filename='backup.db', exclusive=False)
            
            #onto_path.append(os.path.dirname(__file__))
            
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()

            sync_reasoner()
        
            with kiposcrum:
                
                lista_instancias = kiposcrum[input_dado].instances()
        
                num_inst = len(lista_instancias)
                
                status = "OK!"
                
                
                for i in range(len(lista_instancias)):
                    
                    list_nomes.append(lista_instancias[i].Nome[0])
                
                    if not lista_instancias[i].Observacao:
                        list_obs.append("Sem observações")
                    else:
                        list_obs.append(lista_instancias[i].Observacao)
                
                
                for i in range(len(lista_instancias)):
                    objetos_final.append({'instancia':lista_instancias[i],'nome':list_nomes[i], 'obs':list_obs[i]})
                
                
                #myworld.close() # só fecha o bd, deixa as instâncias no bd
        
        except:
            
            status = "Erro!" 
            num_inst = "Desconhecido"
            
            print("Falha de acesso!")
        
        finally:
            
            myworld.close()
        
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

def inserir_instancia_tela_ok(request):
    """ View de confirmação de que uma instância foi adicionada com sucesso.
    
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'inserir_instancia_tela_ok.html'. 
    """
    
    return render(request, 'inserir_instancia_tela_ok.html')

# instancia pra botar + espaço pra definir o nome
def inserir_instancia(request):
    """ View para pegar uma instância a ser adicionada no Banco de Dados.
    
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'instancias_inserir_select.html' ou redirect para view 'inserir_instancia_tela_ok'. 
    """
    

    form = inserir_instancias_tipoForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'input_dado' in request.session:
            del request.session['input_dado']
    
        input_nome = request.POST.get('nome')
        input_classe = request.POST.get('classe')
        input_obs = request.POST.get('observacao')
        
        seed = str(time.time())
        id_unico = faz_id(seed)
        
        # OWLREADY2
        try:
    
            myworld = World(filename='backup.db', exclusive=False)
                
            #onto_path.append(os.path.dirname(__file__))
                
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
            with kiposcrum:
                
                kiposcrum[input_classe](input_nome + id_unico)
                
                kiposcrum[input_nome + id_unico].Nome.append(input_nome)
                
                if input_obs != "":
                    kiposcrum[input_nome + id_unico].Observacao.append(input_obs)
                
                myworld.save()
                
                status = "OK!"
            
        except:
            status = "Erro!"    

        finally:
            myworld.close()
            

        
        
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_nome'] = input_nome
        request.session['input_classe'] = input_classe
        request.session['input_status'] = status
        return redirect('/kipo_playground/inserir_instancia_tela_ok/')
        
    
    return render(request, 'instancias_inserir_select.html', context)


def retirar_instancia(request, instancia):
    
    '''
    form = inserir_instancias_tipoForm()

    context = {'form':form}
    '''
    
    
    input_nome = instancia[5:]
    
    try:
        myworld = World(filename='backup.db', exclusive=False)
                
                
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
        
        sync_reasoner()
        
        with kiposcrum:
                
            # nome ja recuperado
            # recupera classe!
            # deleta instancia!
                
            #input_classe = str(input_nome.is_a.pop(0))
                
            print("------------------")
            #print(input_nome)
            print("------------------")
                
            #destroy_entity(kiposcrum[input_classe](input_nome))
            
            status = "OK!"
            input_classe = "Erro!"
                
    except:
        
        status = "Erro!"    
        input_classe = "Erro!"

    finally:
        
        myworld.close()
    
    request.session['input_nome'] = input_nome
    request.session['input_classe'] = input_classe
    request.session['input_status'] = status
    return render(request, 'inserir_instancia_tela_ok.html')
    

# !MÓDULO DE GESTÃO DE SPRINTS
# !SELECIONA SPRINT
# !------------------------------------------------------------

def sprint_select(request):
    """ View de seleção de Sprints para sua visualização.
    
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'seleciona_sprint.html'. 
    """
    
    objetos_sprints = []
    
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
        
        sync_reasoner()
        
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
            
            
            # era pra ser "kipo.KIPCO__Knowledge_Intensive_Process"
            #objetos_sprints = transforma_objeto(lista_instancias)
            
            # debugar!! No 1 dá ruim quando adiciona algo novo.
            print(str(lista_instancias[0].Nome[0]))
            print(str(lista_instancias[0].is_a.pop(0)))
            print(str(lista_instancias[0].Observacao))
            
            '''
            
            list_nomes = []
            list_classe = []
            list_obs = []
            objetos_final = []
            
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
            print("---------------")
            '''
            
            '''
            for i in range(len(lista_instancias)):
                objetos_final.append({'classe_inst':list_classe[i], 'instancia':str(lista_instancias[i]),'nome':list_nomes[i], 'obs':list_obs[i]})
            '''
            
    except:
            
        status = "Erro!" 
        num_inst = "Desconhecido"
        
        print("---------------------------")
        print("Falha de acesso!")
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        
        print("---------------------------")

    finally:
        
        myworld.close() # só fecha o bd, deixa as instâncias no bd
    
    
    
    request.session['num_inst'] = num_inst
    request.session['status'] = status
        
    context = {"objetos_sprints": objetos_sprints}
    return render(request, 'seleciona_sprint.html', context)


# VER DADOS DA SPRINT
def sprint_dashboard(request, instancia_sprint):
    """ View de seleção de Sprints para sua visualização.
    
        :param request: HTTP Request. 
        :param instancia_sprint: String com Instância a ser visualizada no formato 'nome + id_único'. Exemplo: 'sprint_da_semana1234'. 
    
        :return: Objeto de render de 'sprint_dashboard.html'. 
    """
    
    
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
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
        
        sync_reasoner()
    
    
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
        
    except:
            
        status = "Erro!" 
        num_inst = "Desconhecido"
        num_prop_correlatas = "Desconhecido"
        num_inst = 0
        
        print("Falha de acesso!")
        
    
    finally:
        
        myworld.close() 
        
    
    request.session['num_inst'] = num_inst
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia_sprint":instancia_sprint , "objetos_during":objeto_during, "objetos_has_input":objeto_has_input, "objetos_has_output":objeto_has_output,
                "objetos_has_isexecutedby":objeto_has_isexecutedby, "objetos_INV_simultaneo":objeto_INV_simultaneo}
    
    return render(request, 'sprint_dashboard.html', context)
    
    
def add_classe(request, classe_inst):
    """ View de adiçao de uma nova instancia, dada uma classe.
    
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'instancias_tipo_select.html' ou redirect para view de 'inserir_instancia_tela_ok'. 
    """
    
    form = inserir_instancias_dada_classeForm()

    context = {'form':form}
    
    if request.method == 'POST':
        
        if 'nome' in request.session:
            del request.session['nome']
        if 'observacao' in request.session:
            del request.session['observacao']
            
        input_nome = str(request.POST.get('nome'))
        input_observacao = str(request.POST.get('observacao'))
        
        status = "Erro!"
        
        seed = str(time.time())
        id_unico = faz_id(seed)
        
        
        # OWLREADY2
        try:
            
            myworld = World(filename='backup.db', exclusive=False)
            
            # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
            kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
            sync_reasoner()
        
            print(classe_inst)
            
            with kiposcrum:
                
                kiposcrum[classe_inst](input_nome + id_unico)
                
                if input_observacao != "":
                    kiposcrum[input_nome + id_unico].Observacao.append(input_observacao)
                
                sync_reasoner()
                
                status = "OK!"
                
                
                myworld.save() # persiste na ontologia
        
        except:
            
            print("Falha de acesso!")
            input_nome = "Não foi recuperado"
            input_classe = "Não foi recuperado"
        
        finally:
            
            myworld.close()
            
        # faz query e bota resultado na sessão, um redirect vai botar o resultado
        request.session['input_nome'] = input_nome + id_unico
        request.session['input_classe'] = classe_inst
        request.session['ontologia_status'] = status
        
        return redirect('/kipo_playground/inserir_instancia_tela_ok/')
        
    return render(request, 'instancias_tipo_select.html', context)

# !VISUALIZAÇÃO DE TRABALHO DIÁRIO DENTRO DE UMA SPRINT
# !------------------------------------------------------------

def daily_dashboard(request, instancia_daily):
    """ View de visualizaçao de Trabalho Diário de uma Sprint.
    
        :param request: HTTP Request. 
        :param instancia_daily: String com Instância a ser visualizada no formato 'nome + id_único'. Exemplo: 'daily_dia_29_setembro1234'. 
    
        :return: Objeto de render de 'daily_dashboard.html'. 
    """
    
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
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
        
        sync_reasoner()

        num_inst = 0

        with kiposcrum:
            
            print("Criando dashboard de Sprint!")
            
            
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
        
    except:
            
        status = "Erro!" 
        num_prop_correlatas = "Desconhecido"
        num_inst = "?"
            
        print("Falha de acesso!")
    
    finally:
        
        myworld.close() 
    
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia":instancia_daily , "objeto_inv_during":objeto_inv_during, "objetos_has_input":objeto_has_input, "objetos_has_output":objeto_has_output,
                "objetos_has_isexecutedby":objeto_has_isexecutedby, "objeto_performs":objeto_performs}
    
    
    return render(request, 'daily_dashboard.html', context)
    

# ------------------------------------------------------------


# ------------------------------------------------------------

'''

    
def daily_add(request):
    

'''

    
# !BACKLOGS
#!-----------------------------------------------------

def ver_sprint_backlog(request, instancia_sprint):
    """ View de visualizaçao de Backlog de uma Sprint.
    
        :param request: HTTP Request. 
        :param instancia_sprint: String com Instância a ser visualizada no formato 'nome + id_único'. Exemplo: 'backlog_primeira_sprint1234'. 
    
        :return: Objeto de render de 'backlog_sprint.html'. 
    """
    
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
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
        
        sync_reasoner()
     
        num_inst = 0
    
        
        with kiposcrum:
            
            print("Criando Visualização de Sprint Backlog!")
            
            status = "OK!"
            
            instancia_backlog_sprint = str(kiposcrum[instancia].ontoscrum__has_input.pop(0))
            
            backlog_sprint = instancia_backlog_sprint[5:]
            
            print(backlog_sprint)
            
            propriedades = kiposcrum[backlog_sprint].get_properties()
            print(propriedades)
            num_prop_correlatas = len(propriedades)
            
            
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
            
    except:
        
        status = "Erro!" 
        num_prop_correlatas = "Desconhecido"
        num_inst = "?"
        instancia = "Erro!" 
        
        print("Falha de acesso!")
        
    finally:
        
        myworld.close()
        
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    #context = {"instancia_backlog": instancia_backlog, "objeto_ismanagedby": objeto_ismanagedby, "objeto_contains": objeto_contains}
    
    context = {"instancia_backlog_sprint":instancia_backlog_sprint, "objeto_contains": objeto_contains, "objeto_during": objeto_during, "objeto_has_input": objeto_has_input, "objeto_has_output": objeto_has_output, "objeto_performs": objeto_performs, "objeto_is_executed_by": objeto_is_executed_by}
    
    return render(request, 'backlog_sprint.html', context)


def ver_backlog_produto(request):
    """ View de visualizaçao de Backlog do Produto. No caso de estudo, só tem 1 Backlog de Produto, logo não existe seleção para Backlog de Produto.
    
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'backlog_produto.html'. 
    """
    
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
    
    num_inst = 0
    
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
        
        sync_reasoner()

        with kiposcrum:
            
            # falta o ontoscrum__originator
            # {kipo.Nome, kipo.ontoscrum__originator, kipo.ontoscrum__is_managed_by, kipo.INV_ontoscrum__has_output, 
            # kipo.INV_ontoscrum__has_input, kipo.INV_uses, kipo.INV_ontoscrum__affects, 
            # kipo.ontoscrum__contains, kipo.contains}
            
            print("Criando Visualização de Product Backlog!")
            
            
            # kiposcrum.KIPCO__Agent("desenvolvedornovo")
            
            # add kipo.backlog_sistema_venda_livros9221 contains do_decision na main de testes
            
            instancia_backlog = str(kiposcrum["Product_Backlog"].instances().pop(0))
            
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
        
    except:
            
        status = "Erro!" 
        num_prop_correlatas = "Desconhecido"
        num_inst = "?"
        instancia_backlog = "Erro!"
        instancia = "Erro!" 
        
        print("Falha de acesso!")
        
    finally:
        
        myworld.close() 
    
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia_backlog": instancia_backlog, "objeto_ismanagedby": objeto_ismanagedby, "objeto_contains": objeto_contains}
    
    return render(request, 'backlog_produto.html', context)


# !SELECIONA DECISAO
# !------------------------------------------------------------

def decision_select(request):
    """ View de seleção de Decisão. 
    
        :param request: HTTP Request. 
    
        :return: Objeto de render de 'seleciona_decisao.html'. 
    """
    
    objetos_final = []
    
    list_nomes = []
    list_obs = []
    
    qntd_decisoes_reais = 0
    
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
        
        sync_reasoner()
        
        
        with kiposcrum:
                
            lista_instancias = kiposcrum["DO__Decision"].instances()
            
            num_inst = len(lista_instancias)
            
            print("\n\n\n\n")
            print(lista_instancias)
            print("\n\n\n\n")
                
            status = "OK!"
            
            for i in range(len(lista_instancias)):
                
                if "DO__Decision" in str(lista_instancias[i].is_a):
                        
                    list_nomes.append(lista_instancias[i].Nome[0])
                    
                    if not lista_instancias[i].Observacao:
                        list_obs.append("Sem observações")
                    else:
                        list_obs.append(lista_instancias[i].Observacao)
                    
                    qntd_decisoes_reais = qntd_decisoes_reais + 1
                    
            for i in range(qntd_decisoes_reais):
                objetos_final.append({'instancia':lista_instancias[i],'nome':list_nomes[i], 'obs':list_obs[i]})
            
    except:
            
        status = "Erro!" 
        num_inst = "Desconhecido"
        
        print("---------------------------")
        print("Falha de acesso!")
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(sys.exc_info()[2])
        
        print("---------------------------")

    finally:
        
        myworld.close() # só fecha o bd, deixa as instâncias no bd

    request.session['num_inst'] = num_inst
    request.session['status'] = status
        
    context = {"objetos_final": objetos_final}
    return render(request, 'seleciona_decisao.html', context)


# VER DADOS DA DECISAO
def decision_dashboard(request, instancia_decisao):
    """ View de Visualização de dados da Decisão, com o objetivo de auxiliar na tomada de Decisão. 
    
        :param request: HTTP Request. 
        :param instancia_decisao: String com a Instância da Decisão a ser visualizada no formato "nome + id". Exemplo: "decidir_BD1234". 
        
        :return: Objeto de render de 'decision_dashboard.html'. 
    """
    
    
    if 'num_inst' in request.session:
        del request.session['num_inst']
            
    if 'status' in request.session:
        del request.session['status']
        
    if 'num_prop_correlatas' in request.session:
        del request.session['num_prop_correlatas']
        
    if 'num_inst' in request.session:
        del request.session['num_inst']
        
    num_inst = 0
    
    # OWLREADY2
    try:
            
        myworld = World(filename='backup.db', exclusive=False)
            
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology("http://www.semanticweb.org/fialho/kipo").load()
            
        
        sync_reasoner()
        
        with kiposcrum:
            
            print("Criando dashboard de DO__Decision!")
            
            
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
        
    except:
            
        status = "Erro!" 
        num_inst = "Desconhecido"
        num_prop_correlatas = "Desconhecido"
        num_inst = 0
            
        print("Falha de acesso!")
    
    finally:
        
        myworld.close() 
    
    request.session['num_inst'] = num_inst
    request.session['status'] = status   # "OK!" ou "Erro!"
    request.session['num_prop_correlatas'] = num_prop_correlatas
    request.session['num_inst'] = str(num_inst)
    
    context = {"instancia_decision": instancia_decisao, "objeto_INV_influences": objeto_INV_influences, "objeto_INV_composes": objeto_INV_composes, "objeto_considers": objeto_considers, "objeto_INV_threatens": objeto_INV_threatens}
    
    return render(request, 'decision_dashboard.html', context)
    

# ------------------------------------------------------------

