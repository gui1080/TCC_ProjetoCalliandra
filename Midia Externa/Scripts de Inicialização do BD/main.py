# Guilherme Braga 17/0162290
# Testes de ontologia Scrum, com ontologia do Scrum implementada

from datetime import datetime, timedelta
import time
import traceback
import os
import io
import unittest                 # https://docs.python.org/3/library/unittest.html
from owlready2 import *         # https://pypi.org/project/Owlready2/
import hashlib

## 13/07 
## juntar ontologia do scrum na kipo nova, implementar as coisas da decisão na kipo nova
## atualizar equivalencias
## NO FINAL -> instanciar e atualizar o bd la no projeto final do django

## consertar declara,cão de instancias
# bd update


def faz_id(input_str):
    
    resultado_id = str(abs(hash(input_str)) % (10 ** 4))
    
    if len(resultado_id) == 3:
        
        resultado_id = "0" + resultado_id

    elif len(resultado_id) == 2:

        resultado_id = "00" + resultado_id
    
    elif len(resultado_id) == 1:
    
        resultado_id = "000" + resultado_id
    
    return resultado_id

# Declaração da main
#--------------------------------------------------------------------------

def main():

    #--------------------------------------------------------------------------
    
    print("Removendo BD antigo!")
    
    files = os.listdir('.')
    
    try:
        
        for file in files:
            
            if "backup.db" in file:
                
                os.remove("backup.db")
                time.sleep(3)
                break
                
    
    except: 
        print("Náo foi possível deletar BD antigo!")
    
    print("\nComeço dos Testes.\nAcessando arquivo local de ontologia!\n")
    
    try:
        
        myworld = World(filename='backup.db', exclusive=False)
        
        onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kipo_fialho.owl').load()
        
        # tem q dar sync aqui
        # myworld.save()
        
    except:
        
        print("Erro no começo")
        
    print("------------------------------------")
        
    print("\nListando classes.\n")
    
    with kiposcrum:
        print(list(kiposcrum.classes()))
        
    print("------------------------------------")
        
    
    #--------------------------------------------------------------------------
    # CRIANDO EQUIVALENCIAS
    
    # botei essas equivalencias direto no Protegé!
    '''
    class KIPCO__Agent(kiposcrum.scrumRoles):
        
        equivalent_to = [kiposcrum.ScrumMaster, 
                        kiposcrum.ProductOwner, 
                        kiposcrum.TeamMember, 
                        kiposcrum.Stakeholder]
        
        def se_explique(self): print("Um Scrum Master na Ontologia do Scrum se comporta como Agente na KIPO!")
        
    class KIPCO__ImpactAgent(kiposcrum.scrumRoles):
        
        equivalent_to = [kiposcrum.Stakeholder]
        
        def se_explique(self): print("Um Stakeholder na Ontologia do Scrum se comporta como Agente de Impacto na KIPO!")
    
    class BPO__Data_Object(kiposcrum.scrumArtifacts):
    
        equivalent_to = [kiposcrum.ProductBacklog,
                        kiposcrum.SprintBacklog]
        
        def se_explique(self): print("Um Backlog na Ontologia do Scrum se comporta como Data Object na KIPO!")
    
    class Process_Task(kiposcrum.BPO__Data_Object):
        
        equivalent_to = [kiposcrum.VisionCreation,
                        kiposcrum.ProductRoadMapCreation]
        
        def se_explique(self): print("Um Product Road Map e um Documento de Visão na Ontologia do Scrum se comporta como Data Object na KIPO!")
    
    class KIPCO_Knowledge_Intesive_Activity(kiposcrum.scrum_Daily):
        
        equivalent_to = [kiposcrum.scrum_Daily]
        
        def se_explique(self): print("Um Scrum Daily na Ontologia do Scrum se comporta como Atividade Intensiva em Conhecimento na KIPO!")
    
    class KIPCO_Knowledge_Intesive_Process(kiposcrum.scrum_Sprint):
    
        equivalent_to = [kiposcrum.scrum_Sprint]
        
        def se_explique(self): print("Uma Scrum Sprint na Ontologia do Scrum se comporta como Processo Intensivo em Conhecimento na KIPO!")
    
    '''
    
    seed = str(time.time())
    
    #--------------------------------------------------------------------------
    # CRIANDO INSTÂNCIAS
    
    
    with kiposcrum:
        
        id_unico = faz_id("teste" + seed)
        kiposcrum["KIPCO__Agent"]("gerente1" + id_unico)
        kiposcrum["gerente1" + id_unico].Nome.append("gerente1")
        
        #id_unico = faz_id("desenvolvedor1" + seed)
        kiposcrum["KIPCO__Impact_Agent"]("desenvolvedor1" + id_unico)
        kiposcrum["desenvolvedor1" + id_unico].Nome.append("desenvolvedor1")
        
        #id_unico = faz_id("desenvolvedor2" + seed)
        kiposcrum["KIPCO__Agent"]("desenvolvedor2" + id_unico)
        kiposcrum["desenvolvedor2" + id_unico].Nome.append("desenvolvedor2")
        
        #id_unico = faz_id("desenvolvedor3" + seed)
        kiposcrum["KIPCO__Agent"]("desenvolvedor3" + id_unico)
        kiposcrum["desenvolvedor3" + id_unico].Nome.append("desenvolvedor3")
        
        #id_unico = faz_id("ceo_da_loja" + seed)
        kiposcrum["KIPCO__Impact_Agent"]("ceo_da_loja" + id_unico)
        kiposcrum["ceo_da_loja" + id_unico].Nome.append("ceo_da_loja")
        
        #id_unico = faz_id("implementar_login_django" + seed)
        kiposcrum["Task_Description"]("implementar_login_django" + id_unico)
        kiposcrum["implementar_login_django" + id_unico].Nome.append("implementar_login_django")
        
        #id_unico = faz_id("implementar_tela_django" + seed)
        kiposcrum["Task_Description"]("implementar_tela_django" + id_unico)
        kiposcrum["implementar_tela_django" + id_unico].Nome.append("implementar_tela_django")
        
        #id_unico = faz_id("login_e_cadastro_bd" + seed)
        kiposcrum["Product_Feature"]("login_e_cadastro_bd" + id_unico)
        kiposcrum["login_e_cadastro_bd" + id_unico].Nome.append("login_e_cadastro_bd")
        
        #id_unico = faz_id("primeira_sprint" + seed)
        kiposcrum["Release_Plan"]("primeira_sprint" + id_unico)
        kiposcrum["primeira_sprint" + id_unico].Nome.append("primeira_sprint")
        
        #id_unico = faz_id("tela_login" + seed)
        kiposcrum["Product_Backlog_Item"]("tela_login" + id_unico)
        kiposcrum["tela_login" + id_unico].Nome.append("tela_login")
        kiposcrum["tela_login" + id_unico].StatusItemResolvido.append("1")
        
        # tela_login = kiposcrum.Product_Backlog_Item("tela_login", namespace = kiposcrum, 
        # contains=[primeira_sprint, login_e_cadastro_bd])
        
        kiposcrum["tela_login" + id_unico].ontoscrum__contains.append(kiposcrum["primeira_sprint" + id_unico])
        
        kiposcrum["tela_login" + id_unico].ontoscrum__contains.append(kiposcrum["login_e_cadastro_bd" + id_unico])
        
        
        kiposcrum["tela_login" + id_unico].EstimatedBusinessValue.append( 13 )
        
        #id_unico = faz_id("pagina_placeholder_html_css" + seed)
        kiposcrum["Product_Feature"]("pagina_placeholder_html_css" + id_unico)
        kiposcrum["pagina_placeholder_html_css" + id_unico].Nome.append("pagina_placeholder_html_css")
        
        #id_unico = faz_id("tela_basica" + seed)
        kiposcrum["Product_Backlog_Item"]("tela_basica" + id_unico)
        kiposcrum["tela_basica" + id_unico].Nome.append("tela_basica")
        kiposcrum["tela_basica" + id_unico].StatusItemResolvido.append("0")
        
        #tela_basica = kiposcrum.Product_Backlog_Item("tela_basica", namespace = kiposcrum, 
        # contains=[primeira_sprint, pagina_placeholder_html_css])
        
        kiposcrum["tela_basica" + id_unico].ontoscrum__contains.append(kiposcrum["primeira_sprint" + id_unico])
        
        kiposcrum["tela_basica" + id_unico].ontoscrum__contains.append(kiposcrum["pagina_placeholder_html_css" + id_unico])
        
        
        kiposcrum["tela_basica" + id_unico].EstimatedBusinessValue.append( 8 )
        
        #id_unico = faz_id("alta_escalabilidade_para_muitos_usuarios_novos" + seed)
        kiposcrum["Product_Feature"]("alta_escalabilidade_para_muitos_usuarios_novos" + id_unico)
        kiposcrum["alta_escalabilidade_para_muitos_usuarios_novos" + id_unico].Nome.append("alta_escalabilidade_para_muitos_usuarios_novos")
        
        #id_unico = faz_id("escolha_de_bd" + seed)
        kiposcrum["Product_Backlog_Item"]("escolha_de_bd" + id_unico)
        kiposcrum["escolha_de_bd" + id_unico].Nome.append("escolha_de_bd")
        kiposcrum["escolha_de_bd" + id_unico].StatusItemResolvido.append("0")
        
        #escolha_de_bd = kiposcrum.Product_Backlog_Item("escolha_de_bd", namespace = kiposcrum, 
        # contains=[primeira_sprint, alta_escalabilidade_para_muitos_usuarios_novos])
        
        kiposcrum["escolha_de_bd" + id_unico].ontoscrum__contains.append(kiposcrum["primeira_sprint" + id_unico])
        
        kiposcrum["escolha_de_bd" + id_unico].ontoscrum__contains.append(kiposcrum["alta_escalabilidade_para_muitos_usuarios_novos" + id_unico])
        
        
        kiposcrum["escolha_de_bd" + id_unico].EstimatedBusinessValue.append( 5 )
        
        #id_unico = faz_id("backlog_funcionalidades1" + seed)
        kiposcrum["Sprint_Backlog"]("backlog_funcionalidades1" + id_unico)
        kiposcrum["backlog_funcionalidades1" + id_unico].Nome.append("backlog_funcionalidades1")
        
        #backlog_funcionalidades1 = kiposcrum.BPO__Data_Object("backlog_funcionalidades1", namespace = kiposcrum, 
        # ontoscrum__is_managed_by=[gerente1, desenvolvedor1, desenvolvedor2, desenvolvedor3], 
        # contains = [implementar_tela_django, implementar_login_django])
        
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["desenvolvedor1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["desenvolvedor2" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["desenvolvedor3" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__contains.append(kiposcrum["implementar_tela_django" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__contains.append(kiposcrum["implementar_login_django" + id_unico])
        
        #id_unico = faz_id("backlog_sistema_venda_livros" + seed)
        kiposcrum["Product_Backlog"]("backlog_sistema_venda_livros" + id_unico)
        kiposcrum["backlog_sistema_venda_livros" + id_unico].Nome.append("backlog_sistema_venda_livros")
        
        #backlog_sistema_venda_livros = kiposcrum.Product_Backlog("backlog_sistema_venda_livros", namespace = kiposcrum, 
        # ontoscrum__is_managed_by = [gerente1], 
        # originator=[ceo_da_loja], 
        # contains = [tela_login, tela_basica])       
        
        kiposcrum["backlog_sistema_venda_livros" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["backlog_sistema_venda_livros" + id_unico].ontoscrum__originator.append(kiposcrum["ceo_da_loja" + id_unico])
        kiposcrum["backlog_sistema_venda_livros" + id_unico].ontoscrum__contains.append(kiposcrum["tela_login" + id_unico])
        kiposcrum["backlog_sistema_venda_livros" + id_unico].ontoscrum__contains.append(kiposcrum["tela_basica" + id_unico])
        
        #id_unico = faz_id("impeditivos_funcionalidades_basicas1" + seed)
        kiposcrum["Impedments_Reporting"]("impeditivos_funcionalidades_basicas1" + id_unico)
        kiposcrum["impeditivos_funcionalidades_basicas1" + id_unico].Nome.append("impeditivos_funcionalidades_basicas1")
        
        #id_unico = faz_id("atualizacao_de_tarefas_sprint_funcionalidades1" + seed)
        kiposcrum["Sprint_Tasks_Updating"]("atualizacao_de_tarefas_sprint_funcionalidades1" + id_unico)
        kiposcrum["atualizacao_de_tarefas_sprint_funcionalidades1" + id_unico].Nome.append("atualizacao_de_tarefas_sprint_funcionalidades1")
        
        #id_unico = faz_id("controle_tarefas_sprint_funcionalidades1" + seed)
        kiposcrum["Sprint_Tasks_Control"]("controle_tarefas_sprint_funcionalidades1" + id_unico)
        kiposcrum["controle_tarefas_sprint_funcionalidades1" + id_unico].Nome.append("controle_tarefas_sprint_funcionalidades1")
        
        #id_unico = faz_id("desenvolvimento_feature_funcionalidades1" + seed)
        kiposcrum["Feature_Development"]("desenvolvimento_feature_funcionalidades1" + id_unico)
        kiposcrum["desenvolvimento_feature_funcionalidades1" + id_unico].Nome.append("desenvolvimento_feature_funcionalidades1")
        
        #id_unico = faz_id("criacao_doc_visao" + seed)
        kiposcrum["Vision_Creation"]("criacao_doc_visao" + id_unico)
        kiposcrum["criacao_doc_visao" + id_unico].Nome.append("criacao_doc_visao")
        
        #id_unico = faz_id("timeline_trabalhos" + seed)
        kiposcrum["Product_Roadmap_Creation"]("timeline_trabalhos" + id_unico)
        kiposcrum["timeline_trabalhos" + id_unico].Nome.append("timeline_trabalhos")
        
        #id_unico = faz_id("trabalho_continuo_funcionalidades1" + seed)
        kiposcrum["scrum_Continuous"]("trabalho_continuo_funcionalidades1" + id_unico)
        kiposcrum["trabalho_continuo_funcionalidades1" + id_unico].Nome.append("trabalho_continuo_funcionalidades1")
        
        #id_unico = faz_id("daily_28_setembro_2021" + seed)
        kiposcrum["KIPCO__Knowledge_Intesive_Activity"]("daily_28_setembro_2021" + id_unico)
        kiposcrum["daily_28_setembro_2021" + id_unico].Nome.append("daily_28_setembro_2021")
        
        #daily_28_setembro_2021 = kiposcrum.KIPCO__Knowledge_Intesive_Activity("daily_28_setembro_2021", namespace = kiposcrum, 
        # ontoscrum__is_executed_by=[gerente1, desenvolvedor1, desenvolvedor2, desenvolvedor3], 
        # ontoscrum__has_input=[backlog_funcionalidades1], 
        # ontoscrum__has_output=[backlog_funcionalidades1], 
        # ontoscrum__during=[trabalho_continuo_funcionalidades1], 
        # performs = [desenvolvimento_feature_funcionalidades1, impeditivos_funcionalidades_basicas1])
        
        
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor2" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor3" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__during.append(kiposcrum["trabalho_continuo_funcionalidades1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__performs.append(kiposcrum["desenvolvimento_feature_funcionalidades1" + id_unico])
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__performs.append(kiposcrum["impeditivos_funcionalidades_basicas1" + id_unico])
        
        #id_unico = faz_id("scrumDailyMeeting_28_setembro_2021" + seed)
        kiposcrum["scrum_Daily_Scrum_Meeting"]("scrumDailyMeeting_28_setembro_2021" + id_unico)
        kiposcrum["scrumDailyMeeting_28_setembro_2021" + id_unico].Nome.append("scrumDailyMeeting_28_setembro_2021")
        
        #scrumDailyMeeting_28_setembro_2021 = kiposcrum.scrum_Daily_Scrum_Meeting("scrumDailyMeeting_28_setembro_2021", namespace = kiposcrum, 
        # ontoscrum__during=[daily_28_setembro_2021])
        
        kiposcrum["scrumDailyMeeting_28_setembro_2021" + id_unico].ontoscrum__during.append(kiposcrum["daily_28_setembro_2021" + id_unico])
        
        #id_unico = faz_id("daily_27_setembro_2021" + seed)
        kiposcrum["KIPCO__Knowledge_Intesive_Activity"]("daily_27_setembro_2021" + id_unico)
        kiposcrum["daily_27_setembro_2021" + id_unico].Nome.append("daily_27_setembro_2021")
        
        #daily_27_setembro_2021 = kiposcrum.KIPCO__Knowledge_Intesive_Activity("daily_28_setembro_2021", namespace = kiposcrum, 
        # ontoscrum__is_executed_by=[gerente1, desenvolvedor1, desenvolvedor2, desenvolvedor3], 
        # ontoscrum__has_input=[backlog_funcionalidades1], 
        # ontoscrum__has_output=[backlog_funcionalidades1], 
        # ontoscrum__during=[trabalho_continuo_funcionalidades1], 
        # performs = [desenvolvimento_feature_funcionalidades1, atualizacao_de_tarefas_sprint_funcionalidades1, controle_tarefas_sprint_funcionalidades1])

        
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor2" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor3" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__during.append(kiposcrum["trabalho_continuo_funcionalidades1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__performs.append(kiposcrum["desenvolvimento_feature_funcionalidades1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__performs.append(kiposcrum["atualizacao_de_tarefas_sprint_funcionalidades1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__performs.append(kiposcrum["controle_tarefas_sprint_funcionalidades1" + id_unico])
        
        #id_unico = faz_id("scrumDailyMeeting_27_setembro_2021" + seed)
        kiposcrum["scrum_Daily_Scrum_Meeting"]("scrumDailyMeeting_27_setembro_2021" + id_unico)
        kiposcrum["scrumDailyMeeting_27_setembro_2021" + id_unico].Nome.append("scrumDailyMeeting_27_setembro_2021")
        
        #scrumDailyMeeting_27_setembro_2021 = kiposcrum.scrum_Daily_Scrum_Meeting("scrumDailyMeeting_27_setembro_2021", namespace = kiposcrum, 
        # ontoscrum__during = [daily_27_setembro_2021])
        kiposcrum["scrumDailyMeeting_27_setembro_2021" + id_unico].ontoscrum__during.append(kiposcrum["daily_27_setembro_2021" + id_unico])
        
        #id_unico = faz_id("reuniao_estrategia_produto_final" + seed)
        kiposcrum["scrum_Strategy_Planning_Horizon"]("reuniao_estrategia_produto_final" + id_unico)
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].Nome.append("reuniao_estrategia_produto_final")
        
        #reuniao_estrategia_produto_final = kiposcrum.scrum_Strategy_Planning_Horizon("reuniao_estrategia_produtofinal", namespace = kiposcrum, 
        # ontoscrum__has_input=[backlog_sistema_venda_livros], 
        # ontoscrum__has_output=[backlog_sistema_venda_livros], 
        # performs=[timeline_trabalhos, criacao_doc_visao], 
        # ontoscrum__is_executed_by=[gerente1, desenvolvedor1, desenvolvedor2, desenvolvedor3])
        
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor1" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor2" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor3" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__performs.append(kiposcrum["criacao_doc_visao" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__performs.append(kiposcrum["timeline_trabalhos" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        kiposcrum["reuniao_estrategia_produto_final" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        
        #id_unico = faz_id("definicao_entrega_subprodutos" + seed)
        kiposcrum["Release_Planning"]("definicao_entrega_subprodutos" + id_unico)
        kiposcrum["definicao_entrega_subprodutos" + id_unico].Nome.append("definicao_entrega_subprodutos")
        
        #id_unico = faz_id("atualizacao_backlog_produto" + seed)
        kiposcrum["Backlog_Updating"]("atualizacao_backlog_produto" + id_unico)
        kiposcrum["atualizacao_backlog_produto" + id_unico].Nome.append("atualizacao_backlog_produto")
        
        #atualizacao_backlog_produto = kiposcrum.Backlog_Updating("atualizacao_backlog_produto", namespace = kiposcrum, 
        # affects = [backlog_funcionalidades1, backlog_sistema_venda_livros]) 
        
        kiposcrum["atualizacao_backlog_produto" + id_unico].ontoscrum__affects.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["atualizacao_backlog_produto" + id_unico].ontoscrum__affects.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        
        #id_unico = faz_id("criacao_backlog_produto" + seed)
        kiposcrum["Initial_Backlog_Creation"]("criacao_backlog_produto" + id_unico)
        kiposcrum["criacao_backlog_produto" + id_unico].Nome.append("criacao_backlog_produto")
        
        #id_unico = faz_id("planejamento_lancamento_sistema_venda_livros" + seed)
        kiposcrum["scrum_Release_Planning_Horizon"]("planejamento_lancamento_sistema_venda_livros" + id_unico)
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].Nome.append("planejamento_lancamento_sistema_venda_livros")
        
        #planejamento_lancamento_sistema_venda_livros = kiposcrum.scrum_Release_Planning_Horizon("planejamento_lancamento_sistema_venda_livros", namespace = kiposcrum, 
        # performs=[definicao_entrega_subprodutos, atualizacao_backlog_produto, criacao_backlog_produto], 
        # ontoscrum__during=[reuniao_estrategia_produto_final], 
        # ontoscrum__is_executed_by=[gerente1, desenvolvedor1, desenvolvedor2, desenvolvedor3], 
        # ontoscrum__has_input = [backlog_funcionalidades1, backlog_sistema_venda_livros], 
        # ontoscrum__has_output = [backlog_funcionalidades1, backlog_sistema_venda_livros])
        
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__performs.append(kiposcrum["definicao_entrega_subprodutos" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__performs.append(kiposcrum["atualizacao_backlog_produto" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__performs.append(kiposcrum["criacao_backlog_produto" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__during.append(kiposcrum["reuniao_estrategia_produto_final" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor1" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor2" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor3" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        
        #id_unico = faz_id("sprint_funcionalidades_basicas1" + seed)
        kiposcrum["KIPCO__Knowledge_Intensive_Process"]("sprint_funcionalidades_basicas1" + id_unico)
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].Nome.append("sprint_funcionalidades_basicas1")
        kiposcrum["daily_28_setembro_2021" + id_unico].ontoscrum__simultaneously.append(kiposcrum["sprint_funcionalidades_basicas1" + id_unico])
        kiposcrum["daily_27_setembro_2021" + id_unico].ontoscrum__simultaneously.append(kiposcrum["sprint_funcionalidades_basicas1" + id_unico])
        
        #sprint_funcionalidades_basicas1 = kiposcrum.KIPCO__Knowledge_Intesive_Process("sprint_funcionalidade_basicas1", namespace = kiposcrum, 
        # performs=[impeditivos_funcionalidades_basicas1], 
        # ontoscrum__has_input=[backlog_funcionalidades1], 
        # ontoscrum__has_output=[backlog_funcionalidades1], 
        # ontoscrum__is_executed_by=[gerente1, desenvolvedor1, desenvolvedor2, desenvolvedor3], 
        # ontoscrum__during=[planejamento_lancamento_sistema_venda_livros])
        
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__performs.append(kiposcrum["impeditivos_funcionalidades_basicas1" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_funcionalidades1" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor1" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor2" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["desenvolvedor3" + id_unico])
        kiposcrum["sprint_funcionalidades_basicas1" + id_unico].ontoscrum__during.append(kiposcrum["planejamento_lancamento_sistema_venda_livros" + id_unico])
        
        #id_unico = faz_id("review_sprint_funcionalidades1" + seed)
        kiposcrum["scrum_Sprint_Review_Meeting"]("review_sprint_funcionalidades1" + id_unico)
        kiposcrum["review_sprint_funcionalidades1" + id_unico].Nome.append("review_sprint_funcionalidades1")
        
        #review_sprint_funcionalidades1 = kiposcrum.scrum_Sprint_Review_Meeting("review_sprint_funcionalidades1", namespace = kiposcrum, 
        # finishes=[sprint_funcionalidades_basicas1])
        
        kiposcrum["review_sprint_funcionalidades1" + id_unico].ontoscrum__finishes.append(kiposcrum["sprint_funcionalidades_basicas1" + id_unico])
        
        #id_unico = faz_id("planejamento_sprint_funcionalidades2" + seed)
        kiposcrum["scrum_Sprint_Planning_Meeting"]("planejamento_sprint_funcionalidades2" + id_unico)
        kiposcrum["planejamento_sprint_funcionalidades2" + id_unico].Nome.append("planejamento_sprint_funcionalidades2")
        
        #planejamento_sprint_funcionalidades2 = kiposcrum.scrum_Sprint_Planning_Meeting("planejamento_sprint_funcionalidades2", namespace = kiposcrum,
        # overlaps=[sprint_funcionalidades_basicas1]) 
        
        kiposcrum["planejamento_sprint_funcionalidades2" + id_unico].ontoscrum__overlaps.append(kiposcrum["sprint_funcionalidades_basicas1" + id_unico])

        #id_unico = faz_id("retrospectiva_sprint_funcionalidades1" + seed)
        kiposcrum["scrum_Sprint_Retrospective_Meeting"]("retrospectiva_sprint_funcionalidades1" + id_unico)
        kiposcrum["retrospectiva_sprint_funcionalidades1" + id_unico].Nome.append("retrospectiva_sprint_funcionalidades1")
        
        #retrospectiva_sprint_funcionalidades1 = kiposcrum.scrum_Sprint_Retrospective_Meeting("retrospectiva_sprint_funcionalidades1", namespace = kiposcrum, 
        # before=[planejamento_sprint_funcionalidades2])
        
        kiposcrum["retrospectiva_sprint_funcionalidades1" + id_unico].ontoscrum__before.append(kiposcrum["planejamento_sprint_funcionalidades2" + id_unico])
        
        #id_unico = faz_id("planejamento_sprint_funcionalidades1" + seed)
        kiposcrum["scrum_Sprint_Planning_Meeting"]("planejamento_sprint_funcionalidades1" + id_unico)
        kiposcrum["planejamento_sprint_funcionalidades1" + id_unico].Nome.append("planejamento_sprint_funcionalidades1")
        
        #planejamento_sprint_funcionalidades1 = kiposcrum.scrum_Sprint_Planning_Meeting("planejamento_sprint_funcionalidades1", namespace = kiposcrum, 
        # overlaps=[sprint_funcionalidades_basicas1])
        
        kiposcrum["planejamento_sprint_funcionalidades1" + id_unico].ontoscrum__overlaps.append(kiposcrum["sprint_funcionalidades_basicas1" + id_unico])
        
        
        #id_unico = faz_id("necessidade_manter_eficiencia" + seed)
        kiposcrum["KIPCO__Belief"]("necessidade_manter_eficiencia" + id_unico)
        kiposcrum["necessidade_manter_eficiencia" + id_unico].Nome.append("necessidade_manter_eficiencia")
        
        #id_unico = faz_id( + seed)
        kiposcrum["DO__Evidence"]("ferramentas_simples_melhor_manutencao" + id_unico)
        kiposcrum["ferramentas_simples_melhor_manutencao" + id_unico].Nome.append("ferramentas_simples_melhor_manutencao")
        
        #id_unico = faz_id("ferramentas_simples_melhor_resultado" + seed)
        kiposcrum["DO__Feeling"]("ferramentas_simples_melhor_resultado" + id_unico)
        kiposcrum["ferramentas_simples_melhor_resultado" + id_unico].Nome.append("ferramentas_simples_melhor_resultado")
        
        #ferramentas_simples_melhor_resultado = kiposcrum.DO__Feeling("ferramentas_simples_melhor_resultado", namespace = kiposcrum, 
        # is_motivated_by = [ferramentas_simples_melhor_manutencao], 
        # belongs_to = [desenvolvedor1])
        
        kiposcrum["ferramentas_simples_melhor_resultado" + id_unico].is_motivated_by.append(kiposcrum["ferramentas_simples_melhor_manutencao" + id_unico])
        kiposcrum["ferramentas_simples_melhor_resultado" + id_unico].belongs_to.append(kiposcrum["ferramentas_simples_melhor_manutencao" + id_unico])
        
        #id_unico = faz_id("intencao_escolha_ferramenta" + seed)
        kiposcrum["KIPCO__Intention"]("intencao_escolha_ferramenta" + id_unico)
        kiposcrum["intencao_escolha_ferramenta" + id_unico].Nome.append("intencao_escolha_ferramenta")
        
        #id_unico = faz_id("intencao_escolha_eficiente" + seed)
        kiposcrum["KIPCO__Intention"]("intencao_escolha_eficiente" + id_unico)
        kiposcrum["intencao_escolha_eficiente" + id_unico].Nome.append("intencao_escolha_eficiente")
        
        #intencao_escolha_eficiente = kiposcrum.KIPCO__Intention("intencao_escolha_eficiente", namespace = kiposcrum, 
        # used_intention = [daily_28_setembro_2021])
        
        kiposcrum["intencao_escolha_eficiente" + id_unico].used_intention.append(kiposcrum["daily_28_setembro_2021" + id_unico])
        
        # KIPCO__Agent -> Intention
        kiposcrum["desenvolvedor1" + id_unico].undertakes_to_carry_out.append(kiposcrum["intencao_escolha_ferramenta" + id_unico])
        #desenvolvedor1.undertakes_to_carry_out.append(intencao_escolha_ferramenta)
        
        # KIPCO__Agent -> Intention
        kiposcrum["desenvolvedor1" + id_unico].undertakes_to_carry_out.append(kiposcrum["intencao_escolha_eficiente" + id_unico])
        #desenvolvedor1.undertakes_to_carry_out.append(intencao_escolha_eficiente)
        
        # resolver esse relacionamento!
        kiposcrum["desenvolvedor1" + id_unico].encerrar_atividades.append(kiposcrum["sprint_funcionalidades_basicas1" + id_unico])
        #desenvolvedor1.encerrar_atividades.append(sprint_funcionalidades_basicas1)
        
        #id_unico = faz_id("mongodb_e_mais_simples" + seed)
        kiposcrum["DO__Feeling"]("mongodb_e_mais_simples" + id_unico)
        kiposcrum["mongodb_e_mais_simples" + id_unico].Nome.append("mongodb_e_mais_simples")
        
        #id_unico = faz_id("mongodb_e_mais_simples" + seed)
        kiposcrum["DO__Question"]("qual_melhor_bd" + id_unico)
        kiposcrum["qual_melhor_bd" + id_unico].Nome.append("mongodb_e_mais_simples")
        
        #id_unico = faz_id("definir_bd_da_aplicacao" + seed)
        kiposcrum["KIPCO__Makes_to_Solve"]("definir_bd_da_aplicacao" + id_unico)
        kiposcrum["definir_bd_da_aplicacao" + id_unico].Nome.append("definir_bd_da_aplicacao")
        
        #mongodb_e_mais_simples = kiposcrum.DO__Feeling("mongodb_e_mais_simples", namespace = kiposcrum, 
        # belongs_to = [desenvolvedor1])
        kiposcrum["mongodb_e_mais_simples" + id_unico].belongs_to.append(kiposcrum["desenvolvedor1" + id_unico])
        
        #qual_melhor_bd = kiposcrum.DO__Question("qual_melhor_bd", namespace = kiposcrum, 
        # isEventProperPartOf = [daily_28_setembro_2021]) 
        kiposcrum["qual_melhor_bd" + id_unico].isEventProperPartOf.append(kiposcrum["daily_28_setembro_2021" + id_unico])
        
        ## cade
        #definir_bd_da_aplicacao = kiposcrum.KIPCO__Makes_to_Solve("definir_bd_da_aplicacao", namespace = kiposcrum, 
        # uses_action = [ daily_28_setembro_2021 ], 
        # propositional_content_of = [ qual_melhor_bd ])
        kiposcrum["definir_bd_da_aplicacao" + id_unico].uses_action.append(kiposcrum["daily_28_setembro_2021" + id_unico])
        kiposcrum["definir_bd_da_aplicacao" + id_unico].propositional_content_of.append(kiposcrum["qual_melhor_bd" + id_unico])
        
        
        # FALTA
        kiposcrum["desenvolvedor1" + id_unico].has_action.append(kiposcrum["definir_bd_da_aplicacao" + id_unico])
        #desenvolvedor1.has_action.append(definir_bd_da_aplicacao)
        
        #id_unico = faz_id("escolher_bd" + seed)
        
        #DO__Decision
        kiposcrum["DO__Decision"]("escolher_bd" + id_unico)
        kiposcrum["escolher_bd" + id_unico].Nome.append("escolher_bd")
        kiposcrum["escolher_bd" + id_unico].StatusProblemaResolvido.append("0")
        kiposcrum["daily_28_setembro_2021" + id_unico].ontoscrum__performs.append(kiposcrum["escolher_bd" + id_unico])
        
        kiposcrum["backlog_funcionalidades1" + id_unico].ontoscrum__contains.append(kiposcrum["escolher_bd" + id_unico])
        
        #id_unico = faz_id("ferramentas_mais_usadas_sao_melhores" + seed)
        kiposcrum["DO__Evidence"]("ferramentas_mais_usadas_sao_melhores" + id_unico)
        kiposcrum["ferramentas_mais_usadas_sao_melhores" + id_unico].Nome.append("ferramentas_mais_usadas_sao_melhores")
        
        #id_unico = faz_id("mysql_e_mais_consagrado_na_industria" + seed)
        kiposcrum["DO__Feeling"]("mysql_e_mais_consagrado_na_industria" + id_unico)
        kiposcrum["mysql_e_mais_consagrado_na_industria" + id_unico].Nome.append("mysql_e_mais_consagrado_na_industria")
        
        #mysql_e_mais_consagrado_na_industria = kiposcrum.DO__Feeling("mysql_e_mais_consagrado_na_industria", namespace = kiposcrum, 
        # belongs_to = [ceo_da_loja], 
        # is_motivated_by = [ ferramentas_mais_usadas_sao_melhores ]) 
        
        kiposcrum["mysql_e_mais_consagrado_na_industria" + id_unico].belongs_to.append(kiposcrum["ceo_da_loja" + id_unico])
        kiposcrum["mysql_e_mais_consagrado_na_industria" + id_unico].is_motivated_by.append(kiposcrum["ferramentas_mais_usadas_sao_melhores" + id_unico])
        
        #id_unico = faz_id("seguranca_e_prioridade" + seed)
        kiposcrum["DO__Restriction"]("seguranca_e_prioridade" + id_unico)
        kiposcrum["seguranca_e_prioridade" + id_unico].Nome.append("seguranca_e_prioridade")
        
        #id_unico = faz_id("precisar_mais_velocidade_desenvolvimento" + seed)
        kiposcrum["DO__Restriction"]("precisar_mais_velocidade_desenvolvimento" + id_unico)
        kiposcrum["precisar_mais_velocidade_desenvolvimento" + id_unico].Nome.append("precisar_mais_velocidade_desenvolvimento")
        
        # mental image ou data object -> assertion
        kiposcrum["desenvolvedor1" + id_unico].contributes_to_create.append(kiposcrum["seguranca_e_prioridade" + id_unico])
        #criacao_doc_visao.contributes_to_create.append(seguranca_e_prioridade)
        
        kiposcrum["timeline_trabalhos" + id_unico].contributes_to_create.append(kiposcrum["precisar_mais_velocidade_desenvolvimento" + id_unico])
        #timeline_trabalhos.contributes_to_create.append(precisar_mais_velocidade_desenvolvimento)
        
        # decision -> restriction ou alternative
        kiposcrum["escolher_bd" + id_unico].considers.append(kiposcrum["seguranca_e_prioridade" + id_unico])
        #escolher_bd.considers.append(seguranca_e_prioridade)
        
        kiposcrum["escolher_bd" + id_unico].considers.append(kiposcrum["precisar_mais_velocidade_desenvolvimento" + id_unico])
        #escolher_bd.considers.append(precisar_mais_velocidade_desenvolvimento)
        
        #id_unico = faz_id("experiencias_negativas_mongodb" + seed)
        kiposcrum["KIPCO__Experience"]("experiencias_negativas_mongodb" + id_unico)
        kiposcrum["experiencias_negativas_mongodb" + id_unico].Nome.append("experiencias_negativas_mongodb")
        
        #id_unico = faz_id("ferramenta_com_menos_escalabilidade_mais_antiga" + seed)
        kiposcrum["DO__Risk"]("ferramenta_com_menos_escalabilidade_mais_antiga" + id_unico)
        kiposcrum["ferramenta_com_menos_escalabilidade_mais_antiga" + id_unico].Nome.append("ferramenta_com_menos_escalabilidade_mais_antiga")
        
        #id_unico = faz_id("retrabalho_aprendizado_e_seguranca" + seed)
        kiposcrum["DO__Risk"]("retrabalho_aprendizado_e_seguranca" + id_unico)
        kiposcrum["retrabalho_aprendizado_e_seguranca" + id_unico].Nome.append("retrabalho_aprendizado_e_seguranca")
        
        #id_unico = faz_id("mysql" + seed)
        kiposcrum["DO__Alternative"]("mysql" + id_unico)
        kiposcrum["mysql" + id_unico].Nome.append("mysql")
        
        #id_unico = faz_id("mongodb" + seed)
        kiposcrum["DO__Alternative"]("mongodb" + id_unico)
        kiposcrum["mongodb" + id_unico].Nome.append("mongodb")
        
        # Intention/Communication/Perception -> Message/Activity Goal
        kiposcrum["retrabalho_aprendizado_e_seguranca" + id_unico].propositional_content_of.append(kiposcrum["mongodb" + id_unico])
        #retrabalho_aprendizado_e_seguranca.propositional_content_of.append(mongodb)
        
        kiposcrum["ferramenta_com_menos_escalabilidade_mais_antiga" + id_unico].propositional_content_of.append(kiposcrum["mysql" + id_unico])
        #ferramenta_com_menos_escalabilidade_mais_antiga.propositional_content_of.append(mysql)
        
        #id_unico = faz_id("escalabilidade" + seed)
        kiposcrum["DO__Criterion"]("escalabilidade" + id_unico)
        kiposcrum["escalabilidade" + id_unico].Nome.append("escalabilidade")
        
        #id_unico = faz_id("seguranca" + seed)
        kiposcrum["DO__Criterion"]("seguranca" + id_unico)
        kiposcrum["seguranca" + id_unico].Nome.append("seguranca")
        
        #id_unico = faz_id("permite_maior_escalabilidade" + seed)
        kiposcrum["DO__Advantage"]("permite_maior_escalabilidade" + id_unico)
        kiposcrum["permite_maior_escalabilidade" + id_unico].Nome.append("permite_maior_escalabilidade")
        
        #id_unico = faz_id("modelo_de_privilegios_e_conexoes_codificadas" + seed)
        kiposcrum["DO__Advantage"]("modelo_de_privilegios_e_conexoes_codificadas" + id_unico)
        kiposcrum["modelo_de_privilegios_e_conexoes_codificadas" + id_unico].Nome.append("modelo_de_privilegios_e_conexoes_codificadas")
        
        #id_unico = faz_id("modelo_baseado_em_funcoes_privilegios_flexiveis" + seed)
        kiposcrum["DO__Disadvantage"]("modelo_baseado_em_funcoes_privilegios_flexiveis" + id_unico)
        kiposcrum["modelo_baseado_em_funcoes_privilegios_flexiveis" + id_unico].Nome.append("modelo_baseado_em_funcoes_privilegios_flexiveis")
        
        #id_unico = faz_id("gestao_de_tabelas_mais_complexa" + seed)
        kiposcrum["DO__Disadvantage"]("gestao_de_tabelas_mais_complexa" + id_unico)
        kiposcrum["gestao_de_tabelas_mais_complexa" + id_unico].Nome.append("gestao_de_tabelas_mais_complexa")
        
        #permite_maior_escalabilidade = kiposcrum.DO__Advantage("permite_maior_escalabilidade", namespace = kiposcrum, 
        # according_to = [escalabilidade], 
        # propositional_content_of = [mongodb])
        
        kiposcrum["permite_maior_escalabilidade" + id_unico].according_to.append(kiposcrum["escalabilidade" + id_unico])
        kiposcrum["permite_maior_escalabilidade" + id_unico].propositional_content_of.append(kiposcrum["mongodb" + id_unico])
        
        #modelo_de_privilegios_e_conexoes_codificadas = kiposcrum.DO__Advantage("modelo_de_privilegios_e_conexoes_codificadas", namespace = kiposcrum, 
        # according_to = [seguranca], 
        # propositional_content_of = [mysql])
        
        kiposcrum["modelo_de_privilegios_e_conexoes_codificadas" + id_unico].according_to.append(kiposcrum["seguranca" + id_unico])
        kiposcrum["modelo_de_privilegios_e_conexoes_codificadas" + id_unico].propositional_content_of.append(kiposcrum["mysql" + id_unico])
        
        #modelo_baseado_em_funcoes_privilegios_flexiveis = kiposcrum.DO__Disadvantage("modelo_baseado_em_funcoes_privilegios_flexiveis", namespace = kiposcrum, 
        # according_to = [seguranca], 
        # propositional_content_of = [mongodb])
        
        kiposcrum["modelo_baseado_em_funcoes_privilegios_flexiveis" + id_unico].according_to.append(kiposcrum["seguranca" + id_unico])
        kiposcrum["modelo_baseado_em_funcoes_privilegios_flexiveis" + id_unico].propositional_content_of.append(kiposcrum["mongodb" + id_unico])
        
        #gestao_de_tabelas_mais_complexa = kiposcrum.DO__Disadvantage("gestao_de_tabelas_mais_complexa", namespace = kiposcrum, 
        # according_to = [escalabilidade], 
        # propositional_content_of = [mysql])
        
        kiposcrum["gestao_de_tabelas_mais_complexa" + id_unico].according_to.append(kiposcrum["escalabilidade" + id_unico])
        kiposcrum["gestao_de_tabelas_mais_complexa" + id_unico].propositional_content_of.append(kiposcrum["mysql" + id_unico])
        
        # innovation agent -> alternative
        kiposcrum["desenvolvedor1" + id_unico].proposes.append(kiposcrum["mongodb" + id_unico])
        #desenvolvedor1.proposes.append(mongodb)
        
        kiposcrum["ceo_da_loja" + id_unico].proposes.append(kiposcrum["mysql" + id_unico])
        #ceo_da_loja.proposes.append(mysql)
        
        # ERROS?
        # Intention/Communication/Perception -> Message/Activity Goal
        #ferramenta_com_menos_escalabilidade_mais_antiga.propositional_content_of.append(mysql)
        kiposcrum["ferramenta_com_menos_escalabilidade_mais_antiga" + id_unico].propositional_content_of.append(kiposcrum["mysql" + id_unico])
        
        kiposcrum["retrabalho_aprendizado_e_seguranca" + id_unico].propositional_content_of.append(kiposcrum["mongodb" + id_unico])
        #retrabalho_aprendizado_e_seguranca.propositional_content_of.append(mongodb)
        
        #experiencias_negativas_mongodb = kiposcrum.KIPCO__Experience("experiencias_negativas_mongodb", namespace = kiposcrum, 
        # influences = [ escolher_bd ], 
        # belongs_to = [ ceo_da_loja ])
        
        kiposcrum["experiencias_negativas_mongodb" + id_unico].influences.append(kiposcrum["escolher_bd" + id_unico])
        kiposcrum["experiencias_negativas_mongodb" + id_unico].belongs_to.append(kiposcrum["ceo_da_loja" + id_unico])
        
        #ferramenta_com_menos_escalabilidade_mais_antiga = kiposcrum.DO__Risk("ferramenta_com_menos_escalabilidade_mais_antiga", namespace = kiposcrum, 
        # theatens = [ escolher_bd ])
        
        kiposcrum["ferramenta_com_menos_escalabilidade_mais_antiga" + id_unico].threatens.append(kiposcrum["escolher_bd" + id_unico])
        
        #retrabalho_aprendizado_e_seguranca = kiposcrum.DO__Risk("retrabalho_aprendizado_e_seguranca", namespace = kiposcrum, 
        # theatens = [ escolher_bd ]) 
        
        kiposcrum["retrabalho_aprendizado_e_seguranca" + id_unico].threatens.append(kiposcrum["escolher_bd" + id_unico])
        
        # FALTA
        kiposcrum["escolher_bd" + id_unico].pos_state.append(kiposcrum["mysql" + id_unico])
        #escolher_bd.pos_state.append(mysql)
        
        kiposcrum["escolher_bd" + id_unico].pos_state.append(kiposcrum["mongodb" + id_unico])
        #escolher_bd.pos_state.append(mongodb)
        
        #id_unico = faz_id("usar_mysql" + seed)
        kiposcrum["DO__Discarded_Alternative"]("usar_mysql" + id_unico)
        kiposcrum["usar_mysql" + id_unico].Nome.append("usar_mysql")
        
        #id_unico = faz_id("usar_mongodb" + seed)
        kiposcrum["DO__Chosen_Alternative"]("usar_mongodb" + id_unico)
        kiposcrum["usar_mongodb" + id_unico].Nome.append("usar_mongodb")
        
        ## declarar
        #usar_mysql = kiposcrum.DO__Discarded_Alternative("usar_mysql", namespace = kiposcrum, 
        # uses = [backlog_sistema_venda_livros])
        
        kiposcrum["usar_mysql" + id_unico].uses.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        
        
        ## declarar
        #usar_mongodb = kiposcrum.DO__Chosen_Alternative("usar_mongodb", namespace = kiposcrum, 
        # uses = [backlog_sistema_venda_livros], 
        # composes = [escolher_bd])
        
        kiposcrum["usar_mongodb" + id_unico].uses.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        kiposcrum["usar_mongodb" + id_unico].composes.append(kiposcrum["escolher_bd" + id_unico])
        
        
        # ERROS?
        # alternative -> resource
        kiposcrum["mysql" + id_unico].uses.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        #mysql.uses.append(backlog_sistema_venda_livros)
        
        kiposcrum["mongodb" + id_unico].uses.append(kiposcrum["backlog_sistema_venda_livros" + id_unico])
        #mongodb.uses.append(backlog_sistema_venda_livros)
        
        #id_unico = faz_id("desagradar_stakeholder" + seed)
        kiposcrum["DO__Risk"]("desagradar_stakeholder" + id_unico)
        kiposcrum["desagradar_stakeholder" + id_unico].Nome.append("desagradar_stakeholder")
        
        #id_unico = faz_id("preocupacao_seguranca_dados_menos_estruturados" + seed)
        kiposcrum["DO__Risk"]("preocupacao_seguranca_dados_menos_estruturados" + id_unico)
        kiposcrum["preocupacao_seguranca_dados_menos_estruturados" + id_unico].Nome.append("preocupacao_seguranca_dados_menos_estruturados")
        
        #preocupacao_seguranca_dados_menos_estruturados = kiposcrum.DO__Risk("preocupacao_seguranca_dados_menos_estruturados", namespace = kiposcrum, 
        # propositional_content_of = [usar_mysql])
        
        kiposcrum["preocupacao_seguranca_dados_menos_estruturados" + id_unico].propositional_content_of.append(kiposcrum["usar_mysql" + id_unico])
        
        
        # ERROS?
        # esse contains é do ODD
        kiposcrum["backlog_sistema_venda_livros" + id_unico].contains.append(kiposcrum["escolha_de_bd" + id_unico])
        #backlog_sistema_venda_livros.contains.append(escolha_de_bd)
        
        kiposcrum["escolha_de_bd" + id_unico].contains.append(kiposcrum["alta_escalabilidade_para_muitos_usuarios_novos" + id_unico])
        #escolha_de_bd.contains.append(alta_escalabilidade_para_muitos_usuarios_novos)
        
        
        
        # Sincronização
        #--------------------------------------------------------------------------
        print("Primeira parte concluída!")
        
        print("\n------------------------------------\n")
        print("Sincronização!")
            
        try:
            #kiposcrum.sync()
            sync_reasoner()
        except:
            print("\n\nErro ao sincronizar.\n\n")
        finally:
            print("\n\nSincronização finalizada.\n\n")    
            
        print("\n------------------------------------\n")
        
        myworld.save()
        
        myworld.close()
    
    '''
    # INSTÂNCIAS DA KIPO
    with kiposcrum:
        
        necessidade_manter_eficiencia = kiposcrum.KIPCO__Belief("necessidade_manter_eficiencia", namespace = kiposcrum)
        
        ferramentas_simples_melhor_manutencao = kiposcrum.DO__Evidence("ferramentas_simples_melhor_manutencao", namespace = kiposcrum)
        
        ferramentas_simples_melhor_resultado = kiposcrum.DO__Feeling("ferramentas_simples_melhor_resultado", namespace = kiposcrum, is_motivated_by = [ferramentas_simples_melhor_manutencao], belongs_to = [desenvolvedor1])
        
        ## falta fazer intenção
        intencao_escolha_ferramenta = kiposcrum.KIPCO__Intention("intencao_escolha_ferramenta", namespace = kiposcrum)
        
        intencao_escolha_eficiente = kiposcrum.KIPCO__Intention("intencao_escolha_eficiente", namespace = kiposcrum, used_intention = [daily_28_setembro_2021])
        
        # KIPCO__Agent -> Intention
        desenvolvedor1.undertakes_to_carry_out.append(intencao_escolha_ferramenta)
        
        # KIPCO__Agent -> Intention
        desenvolvedor1.undertakes_to_carry_out.append(intencao_escolha_eficiente)
        
        # resolver esse relacionamento!
        #desenvolvedor1.encerrar_atividades.append(sprint_funcionalidades_basicas1)
        
        mongodb_e_mais_simples = kiposcrum.DO__Feeling("mongodb_e_mais_simples", namespace = kiposcrum, belongs_to = [desenvolvedor1])
        
        qual_melhor_bd = kiposcrum.DO__Question("qual_melhor_bd", namespace = kiposcrum, isEventProperPartOf = [daily_28_setembro_2021]) 
        
        ## cade
        definir_bd_da_aplicacao = kiposcrum.KIPCO__Makes_to_Solve("definir_bd_da_aplicacao", namespace = kiposcrum, uses_action = [ daily_28_setembro_2021 ], propositional_content_of = [ qual_melhor_bd ])
        
        # FALTA
        desenvolvedor1.has_action.append(definir_bd_da_aplicacao)
        
        escolher_bd = kiposcrum.DO__Decision("escolher_bd", namespace = kiposcrum)
        
        ferramentas_mais_usadas_sao_melhores = kiposcrum.DO__Evidence("ferramentas_mais_usadas_sao_melhores", namespace = kiposcrum)
        
        mysql_e_mais_consagrado_na_industria = kiposcrum.DO__Feeling("mysql_e_mais_consagrado_na_industria", namespace = kiposcrum, belongs_to = [ceo_da_loja], is_motivated_by = [ ferramentas_mais_usadas_sao_melhores ]) 
        
        seguranca_e_prioridade = kiposcrum.DO__Restriction("seguranca_e_prioridade", namespace = kiposcrum)
        
        precisar_mais_velocidade_desenvolvimento = kiposcrum.DO__Restriction("precisar_mais_velocidade_desenvolvimento", namespace = kiposcrum)
        
        # mental image ou data object -> assertion
        criacao_doc_visao.contributes_to_create.append(seguranca_e_prioridade)
        
        timeline_trabalhos.contributes_to_create.append(precisar_mais_velocidade_desenvolvimento)
        
        # decision -> restriction ou alternative
        escolher_bd.considers.append(seguranca_e_prioridade)
        
        escolher_bd.considers.append(precisar_mais_velocidade_desenvolvimento)
        
        experiencias_negativas_mongodb = kiposcrum.KIPCO__Experience("experiencias_negativas_mongodb", namespace = kiposcrum, influences = [ escolher_bd ], belongs_to = [ ceo_da_loja ])
        
        ferramenta_com_menos_escalabilidade_mais_antiga = kiposcrum.DO__Risk("ferramenta_com_menos_escalabilidade_mais_antiga", namespace = kiposcrum, theatens = [ escolher_bd ])
        
        retrabalho_aprendizado_e_seguranca = kiposcrum.DO__Risk("retrabalho_aprendizado_e_seguranca", namespace = kiposcrum, theatens = [ escolher_bd ]) 
        
        mysql = kiposcrum.DO__Alternative("mysql", namespace = kiposcrum)
        
        mongodb = kiposcrum.DO__Alternative("mongodb", namespace = kiposcrum)
        
        # Intention/Communication/Perception -> Message/Activity Goal
        retrabalho_aprendizado_e_seguranca.propositional_content_of.append(mongodb)
        
        ferramenta_com_menos_escalabilidade_mais_antiga.propositional_content_of.append(mysql)
        
        escalabilidade = kiposcrum.DO__Criterion("escalabilidade", namespace = kiposcrum)
        
        seguranca = kiposcrum.DO__Criterion("seguranca", namespace = kiposcrum)
        
        permite_maior_escalabilidade = kiposcrum.DO__Advantage("permite_maior_escalabilidade", namespace = kiposcrum, according_to = [escalabilidade], propositional_content_of = [mongodb])
        
        modelo_de_privilegios_e_conexoes_codificadas = kiposcrum.DO__Advantage("modelo_de_privilegios_e_conexoes_codificadas", namespace = kiposcrum, according_to = [seguranca], propositional_content_of = [mysql])
        
        modelo_baseado_em_funcoes_privilegios_flexiveis = kiposcrum.DO__Disadvantage("modelo_baseado_em_funcoes_privilegios_flexiveis", namespace = kiposcrum, according_to = [seguranca], propositional_content_of = [mongodb])
        
        gestao_de_tabelas_mais_complexa = kiposcrum.DO__Disadvantage("gestao_de_tabelas_mais_complexa", namespace = kiposcrum, according_to = [escalabilidade], propositional_content_of = [mysql])
        
        # innovation agent -> alternative
        desenvolvedor1.proposes.append(mongodb)
        
        ceo_da_loja.proposes.append(mysql)
        
        # ERROS?
        # Intention/Communication/Perception -> Message/Activity Goal
        ferramenta_com_menos_escalabilidade_mais_antiga.propositional_content_of.append(mysql)
        
        retrabalho_aprendizado_e_seguranca.propositional_content_of.append(mongodb)
        
        # FALTA
        escolher_bd.pos_state.append(mysql)
        
        escolher_bd.pos_state.append(mongodb)
        
        ## declarar
        usar_mysql = kiposcrum.DO__Discarded_Alternative("usar_mysql", namespace = kiposcrum, uses = [backlog_sistema_venda_livros])
        
        ## declarar
        usar_mongodb = kiposcrum.DO__Chosen_Alternative("usar_mongodb", namespace = kiposcrum, uses = [backlog_sistema_venda_livros], composes = [escolher_bd])
        
        # FALTA
        escolher_bd.pos_state.append(usar_mysql)
        
        escolher_bd.pos_state.append(usar_mongodb)
        
        # ERROS?
        # alternative -> resource
        mysql.uses.append(backlog_sistema_venda_livros)
        
        mongodb.uses.append(backlog_sistema_venda_livros)
        
        desagradar_stakeholder = kiposcrum.DO__Risk("desagradar_stakeholder", namespace = kiposcrum)
        
        preocupacao_seguranca_dados_menos_estruturados = kiposcrum.DO__Risk("preocupacao_seguranca_dados_menos_estruturados", namespace = kiposcrum, propositional_content_of = [usar_mysql])
        
        # ERROS?
        # esse contains é do ODD
        backlog_sistema_venda_livros.contains.append(escolha_de_bd)
        
        escolha_de_bd.contains.append(alta_escalabilidade_para_muitos_usuarios_novos)
        
        kiposcrum.save()    
    
    # DEMONSTRANDO EQUIVALÊNCIA!
    print("------------------------------------")
    
    print("\nAcessando classe BPO Data Object.\n")
    print(str(kiposcrum.BPO__Data_Object))
    
    print("\nMas o que é BPO Data Object?\n")
    print(str(kiposcrum.BPO__Data_Object.is_a))
        
    print("\nAcessando o indivíduo instanciado como Product Backlog.\n")
    print(str( backlog_sistema_venda_livros.is_a))
    
    print("Qual é a classe de 'backlog_sistema_venda_livros'?")
    print(str(backlog_sistema_venda_livros.__class__))
    
    print("\nOu seja, foi possível fazer a relação de equivalência entre ontologias!\n\nBPO Data Object -> ProductBacklog!")
    
    print("------------------------------------")
    
    # Realizando testes
    #--------------------------------------------------------------------------
    
    #####
    '''
    

    
if __name__ == '__main__':
    
    # contabiliza o tempo de execução!
    inicio = time.time()
    main()
    fim = time.time()

    duracao = (fim - inicio)/60
    print("\n\n\nFim da execução!\n\nDuração da execução deste script: %f minutos." % (duracao) + "\n\n")
    
    
