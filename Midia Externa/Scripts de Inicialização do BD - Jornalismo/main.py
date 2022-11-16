from datetime import datetime, timedelta
import time
import traceback
import os
import io
import unittest                 # https://docs.python.org/3/library/unittest.html
from owlready2 import *         # https://pypi.org/project/Owlready2/
import hashlib


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
    
    
    seed = str(time.time())
    
    #--------------------------------------------------------------------------
    # CRIANDO INSTÂNCIAS
    
    
    with kiposcrum:
        
        # tcc_casodeestudo_jornalismo.png
        # intancias
        
        id_unico = faz_id("teste" + seed)
        
        kiposcrum["KIPCO__Agent"]("gerente1" + id_unico)
        kiposcrum["gerente1" + id_unico].Nome.append("gerente1")
        
        kiposcrum["KIPCO__Agent"]("jornalista1" + id_unico)
        kiposcrum["jornalista1" + id_unico].Nome.append("jornalista1")
        
        kiposcrum["KIPCO__Agent"]("jornalista2" + id_unico)
        kiposcrum["jornalista2" + id_unico].Nome.append("jornalista2")
        
        kiposcrum["KIPCO__Agent"]("representante_investidores" + id_unico)
        kiposcrum["representante_investidores" + id_unico].Nome.append("representante_investidores")
        
        kiposcrum["KIPCO__Agent"]("gerente1" + id_unico)
        kiposcrum["fotografo1" + id_unico].Nome.append("fotografo1")
        
        # -------------------------------
        
        kiposcrum["DO__Decision"]("escolher_novo_BD_cedoc" + id_unico)
        kiposcrum["escolher_novo_BD_cedoc" + id_unico].Nome.append("escolher_novo_BD_cedoc")
        
        kiposcrum["DO__Decision"]("decidir_materia_destaque_setembro" + id_unico)
        kiposcrum["decidir_materia_destaque_setembro" + id_unico].Nome.append("decidir_materia_destaque_setembro")
        
        # -------------------------------
        
        kiposcrum["Sprint_Tasks_Updating"]("atualizacao_tarefas_sprint_final_de_setembro" + id_unico)
        kiposcrum["atualizacao_tarefas_sprint_final_de_setembro" + id_unico].Nome.append("atualizacao_tarefas_sprint_final_de_setembro")
        
        
        kiposcrum["Sprint_Tasks_Control"]("controle_tarefas_sprint_final_de_setembro" + id_unico)
        kiposcrum["controle_tarefas_sprint_final_de_setembro" + id_unico].Nome.append("controle_tarefas_sprint_final_de_setembro")
        
        
        kiposcrum["Feature_Development"]("desenvolvimento_software_para_final_de_setembro" + id_unico)
        kiposcrum["desenvolvimento_software_para_final_de_setembro" + id_unico].Nome.append("desenvolvimento_software_para_final_de_setembro")
        
        kiposcrum["Impedments_Reporting"]("impeditivos_reconhecidos_para_final_de_setembro" + id_unico)
        kiposcrum["impeditivos_reconhecidos_para_final_de_setembro" + id_unico].Nome.append("impeditivos_reconhecidos_para_final_de_setembro")
        
        # -------------------------------
        
        kiposcrum["scrum_Daily_Scrum_Meeting"]("reuniao_28_09_2021" + id_unico)
        kiposcrum["reuniao_28_09_2021" + id_unico].Nome.append("reuniao_28_09_2021")
        
        kiposcrum["Sprint_Backlog"]("backlog_final_terceiro_trimestre_2021" + id_unico)
        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].Nome.append("backlog_final_terceiro_trimestre_2021")
        
        kiposcrum["scrum_Daily"]("tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico)
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].Nome.append("tarefas_final_terceiro_trimestre_2021_dia_28_09_2021")
        
        kiposcrum["scrum_Continuous"]("trabalho_continuo_para_conclusao_final_terceiro_trimestre_2021" + id_unico)
        kiposcrum["trabalho_continuo_para_conclusao_final_terceiro_trimestre_2021" + id_unico].Nome.append("trabalho_continuo_para_conclusao_final_terceiro_trimestre_2021")
        
        kiposcrum["scrum_Daily"]("tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico)
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].Nome.append("tarefas_final_terceiro_trimestre_2021_dia_27_09_2021")
        
        kiposcrum["scrum_Daily_Scrum_Meeting"]("reuniao_27_09_2021" + id_unico)
        kiposcrum["reuniao_27_09_2021" + id_unico].Nome.append("reuniao_27_09_2021")
        
        # -------------------------------
        
        kiposcrum["scrum_Strategy_Planning_Horizon"]("reuniao_estrategica_para_obter_produto_final" + id_unico)
        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].Nome.append("reuniao_estrategica_para_obter_produto_final")
        
        kiposcrum["Vision_Creation"]("doc_visao_redacao_2021" + id_unico)
        kiposcrum["doc_visao_redacao_2021" + id_unico].Nome.append("doc_visao_redacao_2021")
        
        kiposcrum["Product_Roadmap_Creation"]("timeline_trabalhos_2021" + id_unico)
        kiposcrum["timeline_trabalhos_2021" + id_unico].Nome.append("timeline_trabalhos_2021")
        
        kiposcrum["Product_Backlog"]("backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico)
        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].Nome.append("backlog_de_desenvolvimento_redacao_jornalista_2021")
        
        #----
        
        kiposcrum["scrum_Release_Planning_Horizon"]("planejamento_lancamento_de_destaques_de_setembro" + id_unico)
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].Nome.append("planejamento_lancamento_de_destaques_de_setembro")
        
        kiposcrum["Release_Planning"]("definicao_de_datas_para_lancamentos_de_materias" + id_unico)
        kiposcrum["definicao_de_datas_para_lancamentos_de_materias" + id_unico].Nome.append("definicao_de_datas_para_lancamentos_de_materias")
        
        kiposcrum["Backlog_Updating"]("atualizacao_periodica_materia_jornalistica_para_2021" + id_unico)
        kiposcrum["atualizacao_periodica_materia_jornalistica_para_2021" + id_unico].Nome.append("atualizacao_periodica_materia_jornalistica_para_2021")
        
        kiposcrum["Initial_Backlog_Creation"]("criacao_backlog_para_redacao_2021" + id_unico)
        kiposcrum["criacao_backlog_para_redacao_2021" + id_unico].Nome.append("criacao_backlog_para_redacao_2021")
        
        # -------------------------------
        
        kiposcrum["scrum_Sprint"]("final_terceiro_trimestre_2021" + id_unico)
        kiposcrum["final_terceiro_trimestre_2021" + id_unico].Nome.append("final_terceiro_trimestre_2021")
        
        kiposcrum["scrum_Sprint_Planning_Meeting"]("" + id_unico)
        kiposcrum["" + id_unico].Nome.append("")
        
        kiposcrum["scrum_Sprint_Planning_Meeting"]("" + id_unico)
        kiposcrum["" + id_unico].Nome.append("")
        
        kiposcrum["Sprint_Retrospective"]("" + id_unico)
        kiposcrum["" + id_unico].Nome.append("")
        
        kiposcrum["scrum_Sprint_Review_Meeting"]("" + id_unico)
        kiposcrum["" + id_unico].Nome.append("")

        kiposcrum["scrum_Release_Planning_Horizon"]("" + id_unico)
        kiposcrum["" + id_unico].Nome.append("")
        
        # -------------------------------
        
        kiposcrum["Product_Backlog_Item"]("definir_contrato_de_patrocinio_com_nova_empresa" + id_unico)
        kiposcrum["definir_contrato_de_patrocinio_com_nova_empresa" + id_unico].Nome.append("definir_contrato_de_patrocinio_com_nova_empresa")
        
        kiposcrum["Product_Feature"]("formalizacao_de_contrato_para_aumento_de_verba" + id_unico)
        kiposcrum["formalizacao_de_contrato_para_aumento_de_verba" + id_unico].Nome.append("formalizacao_de_contrato_para_aumento_de_verba")
        
        kiposcrum["Release_Plan"]("executar_ou_abandonar_contrato_ate_final_2021" + id_unico)
        kiposcrum["executar_ou_abandonar_contrato_ate_final_2021" + id_unico].Nome.append("executar_ou_abandonar_contrato_ate_final_2021")
        
        kiposcrum["Product_Backlog_Item"]("executar_obra_departamento_de_ti" + id_unico)
        kiposcrum["executar_obra_departamento_de_ti" + id_unico].Nome.append("executar_obra_departamento_de_ti")
        
        kiposcrum["Product_Feature"]("adaptacao_de_infraestrutura_para_servidores" + id_unico)
        kiposcrum["adaptacao_de_infraestrutura_para_servidores" + id_unico].Nome.append("adaptacao_de_infraestrutura_para_servidores")
        
        kiposcrum["Release_Plan"]("antes_de_decidir_qual_BD_sera_usado" + id_unico)
        kiposcrum["antes_de_decidir_qual_BD_sera_usado" + id_unico].Nome.append("antes_de_decidir_qual_BD_sera_usado")
        
        kiposcrum["Product_Backlog_Item"]("escolha_de_BD_a_ser_usado" + id_unico)
        kiposcrum["escolha_de_BD_a_ser_usado" + id_unico].Nome.append("escolha_de_BD_a_ser_usado")
        
        kiposcrum["Product_Feature"]("alta_escalabilidade_para_gestao_de_dados" + id_unico)
        kiposcrum["alta_escalabilidade_para_gestao_de_dados" + id_unico].Nome.append("alta_escalabilidade_para_gestao_de_dados")
        
        kiposcrum["Release_Plan"]("ao_final_de_setembro" + id_unico)
        kiposcrum["ao_final_de_setembro" + id_unico].Nome.append("ao_final_de_setembro")
        
        kiposcrum["Product_Backlog_Item"]("definicao_materia_destaque_de_setembro" + id_unico)
        kiposcrum["definicao_materia_destaque_de_setembro" + id_unico].Nome.append("definicao_materia_destaque_de_setembro")
        
        kiposcrum["Product_Feature"]("materia_destaque_que_nao_ofusca_outras_ocorrencias_e_gera_receita" + id_unico)
        kiposcrum["materia_destaque_que_nao_ofusca_outras_ocorrencias_e_gera_receita" + id_unico].Nome.append("materia_destaque_que_nao_ofusca_outras_ocorrencias_e_gera_receita")
        
        kiposcrum["Release_Plan"]("lancamento_final_de_setembro" + id_unico)
        kiposcrum["lancamento_final_de_setembro" + id_unico].Nome.append("lancamento_final_de_setembro")
        
        # -------------------------------
        
        # tcc_casodeestudo_jornalismo.png
        # relacionamentos
        
        
        # -------------------------------
        
        
        
        
        # -------------------------------
        
        
        
        
        # -------------------------------
        
        
        
        # -------------------------------
        
        
        
        # -------------------------------
        