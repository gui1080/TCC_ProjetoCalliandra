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

        # -------------------------------
        # -------------------------------
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

        kiposcrum["KIPCO__Agent"]("fotografo1" + id_unico)
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

        kiposcrum["Task_Description"]("refatorar_coluna_jornalista2" + id_unico)
        kiposcrum["refatorar_coluna_jornalista2" + id_unico].Nome.append("refatorar_coluna_jornalista2")
        kiposcrum["refatorar_coluna_jornalista2" + id_unico].Observacao.append("Jornalista2 é responsável pela possível matéria destaque de setembro.")

        kiposcrum["Task_Description"]("definir_estrategia_postagem_redes_sociais" + id_unico)
        kiposcrum["definir_estrategia_postagem_redes_sociais" + id_unico].Nome.append("definir_estrategia_postagem_redes_sociais")
        kiposcrum["definir_estrategia_postagem_redes_sociais" + id_unico].Observacao.append("Estratégia bem definida em mais de uma rede social vai ajudar a agregar valor para a Redação Jornalística.")


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

        kiposcrum["scrum_Sprint_Planning_Meeting"]("reuniao_planejamento_quarto_trimestre_2021" + id_unico)
        kiposcrum["reuniao_planejamento_quarto_trimestre_2021" + id_unico].Nome.append("reuniao_planejamento_quarto_trimestre_2021")

        kiposcrum["scrum_Sprint_Retrospective_Meeting"]("revisao_de_objetivos_alcancados_terceiro_trimestre" + id_unico)
        kiposcrum["revisao_de_objetivos_alcancados_terceiro_trimestre" + id_unico].Nome.append("revisao_de_objetivos_alcancados_terceiro_trimestre")

        kiposcrum["scrum_Sprint_Review_Meeting"]("review_terceiro_trimestre" + id_unico)
        kiposcrum["review_terceiro_trimestre" + id_unico].Nome.append("review_terceiro_trimestre")

        kiposcrum["scrum_Sprint_Planning_Meeting"]("planejamento_inicial_de_tarefas_para_terceiro_trimestre" + id_unico)
        kiposcrum["planejamento_inicial_de_tarefas_para_terceiro_trimestre" + id_unico].Nome.append("planejamento_inicial_de_tarefas_para_terceiro_trimestre")

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
        # -------------------------------

        # tcc_casodeestudo_jornalismo.png
        # relacionamentos

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista1" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista2" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["fotografo1" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__performs.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__performs.append(kiposcrum["escolher_novo_BD_cedoc" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__performs.append(kiposcrum["impeditivos_reconhecidos_para_final_de_setembro" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__performs.append(kiposcrum["desenvolvimento_software_para_final_de_setembro" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__during.append(kiposcrum["trabalho_continuo_para_conclusao_final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__simultaneously.append(kiposcrum["final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["reuniao_28_09_2021" + id_unico].ontoscrum__during.append(kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico])



        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista1" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista2" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["fotografo1" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__performs.append(kiposcrum["desenvolvimento_software_para_final_de_setembro" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__during.append(kiposcrum["trabalho_continuo_para_conclusao_final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["final_terceiro_trimestre_2021" + id_unico].ontoscrum__during.append(kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico])


        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_27_09_2021" + id_unico].ontoscrum__simultaneously.append(kiposcrum["final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["reuniao_27_09_2021" + id_unico].ontoscrum__during.append(kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico])

        # -------------------------------

        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])
        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])

        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__performs.append(kiposcrum["timeline_trabalhos_2021" + id_unico])
        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__performs.append(kiposcrum["doc_visao_redacao_2021" + id_unico])

        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista1" + id_unico])
        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista2" + id_unico])
        kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["fotografo1" + id_unico])


        # -------------------------------

        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__during.append(kiposcrum["reuniao_estrategica_para_obter_produto_final" + id_unico])

        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista1" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["jornalista2" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__is_executed_by.append(kiposcrum["fotografo1" + id_unico])

        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__performs.append(kiposcrum["definicao_de_datas_para_lancamentos_de_materias" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__performs.append(kiposcrum["atualizacao_periodica_materia_jornalistica_para_2021" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__performs.append(kiposcrum["criacao_backlog_para_redacao_2021" + id_unico])

        # -------------------------------

        kiposcrum["atualizacao_periodica_materia_jornalistica_para_2021" + id_unico].ontoscrum__affects.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["atualizacao_periodica_materia_jornalistica_para_2021" + id_unico].ontoscrum__affects.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])

        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])

        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["planejamento_lancamento_de_destaques_de_setembro" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])

        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].ontoscrum__contains.append(kiposcrum["refatorar_coluna_jornalista2" + id_unico])
        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].ontoscrum__contains.append(kiposcrum["definir_estrategia_postagem_redes_sociais" + id_unico])

        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["jornalista1" + id_unico])
        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["jornalista2" + id_unico])
        kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["fotografo1" + id_unico])

        # -------------------------------

        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].ontoscrum__is_managed_by.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].ontoscrum__originator.append(kiposcrum["representante_investidores" + id_unico])

        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].ontoscrum__contains.append(kiposcrum["definicao_materia_destaque_de_setembro" + id_unico])
        kiposcrum["definicao_materia_destaque_de_setembro" + id_unico].ontoscrum__contains.append(kiposcrum["materia_destaque_que_nao_ofusca_outras_ocorrencias_e_gera_receita" + id_unico])
        kiposcrum["definicao_materia_destaque_de_setembro" + id_unico].ontoscrum__contains.append(kiposcrum["lancamento_final_de_setembro" + id_unico])
        kiposcrum["definicao_materia_destaque_de_setembro" + id_unico].EstimatedBusinessValue.append( 13 )
        kiposcrum["definicao_materia_destaque_de_setembro" + id_unico].StatusItemResolvido.append( 0 )


        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].ontoscrum__contains.append(kiposcrum["escolha_de_BD_a_ser_usado" + id_unico])
        kiposcrum["escolha_de_BD_a_ser_usado" + id_unico].ontoscrum__contains.append(kiposcrum["alta_escalabilidade_para_gestao_de_dados" + id_unico])
        kiposcrum["escolha_de_BD_a_ser_usado" + id_unico].ontoscrum__contains.append(kiposcrum["ao_final_de_setembro" + id_unico])
        kiposcrum["escolha_de_BD_a_ser_usado" + id_unico].EstimatedBusinessValue.append( 5 )
        kiposcrum["escolha_de_BD_a_ser_usado" + id_unico].StatusItemResolvido.append( 1 )


        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].ontoscrum__contains.append(kiposcrum["executar_obra_departamento_de_ti" + id_unico])
        kiposcrum["executar_obra_departamento_de_ti" + id_unico].ontoscrum__contains.append(kiposcrum["adaptacao_de_infraestrutura_para_servidores" + id_unico])
        kiposcrum["executar_obra_departamento_de_ti" + id_unico].ontoscrum__contains.append(kiposcrum["antes_de_decidir_qual_BD_sera_usado" + id_unico])
        kiposcrum["executar_obra_departamento_de_ti" + id_unico].EstimatedBusinessValue.append( 2 )
        kiposcrum["executar_obra_departamento_de_ti" + id_unico].StatusItemResolvido.append( 1 )


        kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico].ontoscrum__contains.append(kiposcrum["definir_contrato_de_patrocinio_com_nova_empresa" + id_unico])
        kiposcrum["definir_contrato_de_patrocinio_com_nova_empresa" + id_unico].ontoscrum__contains.append(kiposcrum["formalizacao_de_contrato_para_aumento_de_verba" + id_unico])
        kiposcrum["definir_contrato_de_patrocinio_com_nova_empresa" + id_unico].ontoscrum__contains.append(kiposcrum["executar_ou_abandonar_contrato_ate_final_2021" + id_unico])
        kiposcrum["definir_contrato_de_patrocinio_com_nova_empresa" + id_unico].EstimatedBusinessValue.append( 8 )
        kiposcrum["definir_contrato_de_patrocinio_com_nova_empresa" + id_unico].StatusItemResolvido.append( 1 )

        # -------------------------------

        kiposcrum["reuniao_planejamento_quarto_trimestre_2021" + id_unico].ontoscrum__overlaps.append(kiposcrum["final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["planejamento_inicial_de_tarefas_para_terceiro_trimestre" + id_unico].ontoscrum__overlaps.append(kiposcrum["final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["revisao_de_objetivos_alcancados_terceiro_trimestre" + id_unico].ontoscrum__before.append(kiposcrum["reuniao_planejamento_quarto_trimestre_2021" + id_unico])

        kiposcrum["review_terceiro_trimestre" + id_unico].ontoscrum__finishes.append(kiposcrum["final_terceiro_trimestre_2021" + id_unico])

        kiposcrum["final_terceiro_trimestre_2021" + id_unico].ontoscrum__has_output.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])
        kiposcrum["final_terceiro_trimestre_2021" + id_unico].ontoscrum__has_input.append(kiposcrum["backlog_final_terceiro_trimestre_2021" + id_unico])

        # -------------------------------
        # -------------------------------
        # tcc_casodeestudo_KIPO_decidirmateria.png
        # intancias

        # kiposcrum["DO__Decision"]("decidir_materia_destaque_setembro" + id_unico)

        kiposcrum["KIPCO__Intention"]("resolver_impasse_rapidamente" + id_unico)
        kiposcrum["resolver_impasse_rapidamente" + id_unico].Nome.append("resolver_impasse_rapidamente")

        kiposcrum["KIPCO__Intention"]("gerar_renda_para_redacao_jornalistica" + id_unico)
        kiposcrum["gerar_renda_para_redacao_jornalistica" + id_unico].Nome.append("gerar_renda_para_redacao_jornalistica")

        kiposcrum["KIPCO__Belief"]("necessidade_de_pagar_contas_na_redacao_jornalistica" + id_unico)
        kiposcrum["necessidade_de_pagar_contas_na_redacao_jornalistica" + id_unico].Nome.append("necessidade_de_pagar_contas_na_redacao_jornalistica")

        kiposcrum["DO__Feeling"]("liberdade_de_expressao_deve_ser_pilar_central_do_trabalho" + id_unico)
        kiposcrum["liberdade_de_expressao_deve_ser_pilar_central_do_trabalho" + id_unico].Nome.append("liberdade_de_expressao_deve_ser_pilar_central_do_trabalho")

        kiposcrum["DO__Feeling"]("materias_boas_sempre_devem_ser_publicadas" + id_unico)
        kiposcrum["materias_boas_sempre_devem_ser_publicadas" + id_unico].Nome.append("materias_boas_sempre_devem_ser_publicadas")

        kiposcrum["DO__Evidence"]("ate_agora_nenhum_risco_justificou_nao_publicar_boa_materia" + id_unico)
        kiposcrum["ate_agora_nenhum_risco_justificou_nao_publicar_boa_materia" + id_unico].Nome.append("ate_agora_nenhum_risco_justificou_nao_publicar_boa_materia")

        kiposcrum["DO__Question"]("a_materia_polemica_do_jornalista2_deveria_ser_publicada?" + id_unico)
        kiposcrum["a_materia_polemica_do_jornalista2_deveria_ser_publicada?" + id_unico].Nome.append("a_materia_polemica_do_jornalista2_deveria_ser_publicada?")

        kiposcrum["KIPCO__Makes_to_Solve"]("definir_materia" + id_unico)
        kiposcrum["definir_materia" + id_unico].Nome.append("definir_materia")

        kiposcrum["KIPCO__Experience"]("experiencia_negativa_com_jornalista2" + id_unico)
        kiposcrum["experiencia_negativa_com_jornalista2" + id_unico].Nome.append("experiencia_negativa_com_jornalista2")

        kiposcrum["DO__Restriction"]("apenas_se_publica_bom_jornalismo" + id_unico)
        kiposcrum["apenas_se_publica_bom_jornalismo" + id_unico].Nome.append("apenas_se_publica_bom_jornalismo")

        kiposcrum["DO__Restriction"]("um_processo_judicial_deve_ser_evitado_por_ocupar_tempo" + id_unico)
        kiposcrum["um_processo_judicial_deve_ser_evitado_por_ocupar_tempo" + id_unico].Nome.append("um_processo_judicial_deve_ser_evitado_por_ocupar_tempo")

        kiposcrum["DO__Feeling"]("materia_que_desagrada_grupo_pode_ser_prejudicial" + id_unico)
        kiposcrum["materia_que_desagrada_grupo_pode_ser_prejudicial" + id_unico].Nome.append("materia_que_desagrada_grupo_pode_ser_prejudicial")

        kiposcrum["DO__Evidence"]("patrocinios_foram_perdidos_antes_por_conta_de_atritos_semelhantes" + id_unico)
        kiposcrum["patrocinios_foram_perdidos_antes_por_conta_de_atritos_semelhantes" + id_unico].Nome.append("patrocinios_foram_perdidos_antes_por_conta_de_atritos_semelhantes")

        kiposcrum["DO__Feeling"]("uma_materia_muito_polemica_afeta_reputacao_do_jornal_no_longo_prazo" + id_unico)
        kiposcrum["uma_materia_muito_polemica_afeta_reputacao_do_jornal_no_longo_prazo" + id_unico].Nome.append("uma_materia_muito_polemica_afeta_reputacao_do_jornal_no_longo_prazo")


        # -------------------------------

        # sobre a decisão

        kiposcrum["DO__Risk"]("risco_de_perder_relevancia_por_desperdicar_oportunidade_de_engajamento" + id_unico)
        kiposcrum["risco_de_perder_relevancia_por_desperdicar_oportunidade_de_engajamento" + id_unico].Nome.append("risco_de_perder_relevancia_por_desperdicar_oportunidade_de_engajamento")

        kiposcrum["DO__Risk"]("risco_de_desagradar_grupos_relevantes_por_assunto_da_noticia" + id_unico)
        kiposcrum["risco_de_desagradar_grupos_relevantes_por_assunto_da_noticia" + id_unico].Nome.append("risco_de_desagradar_grupos_relevantes_por_assunto_da_noticia")

        kiposcrum["DO__Criterion"]("riscos_legais" + id_unico)
        kiposcrum["riscos_legais" + id_unico].Nome.append("riscos_legais")

        kiposcrum["DO__Advantage"]("corte_de_gastos_em_caso_de_processo" + id_unico)
        kiposcrum["corte_de_gastos_em_caso_de_processo" + id_unico].Nome.append("corte_de_gastos_em_caso_de_processo")

        kiposcrum["DO__Disadvantage"]("materia_polemica_por_se_tratar_de_algo_que_desfavorece_um_grupo" + id_unico)
        kiposcrum["materia_polemica_por_se_tratar_de_algo_que_desfavorece_um_grupo" + id_unico].Nome.append("materia_polemica_por_se_tratar_de_algo_que_desfavorece_um_grupo")

        kiposcrum["DO__Alternative"]("publicar_materia_jornalista_2" + id_unico)
        kiposcrum["publicar_materia_jornalista_2" + id_unico].Nome.append("publicar_materia_jornalista_2")

        # -------------------------------

        kiposcrum["DO__Criterion"]("engajamento" + id_unico)
        kiposcrum["engajamento" + id_unico].Nome.append("engajamento")

        kiposcrum["DO__Advantage"]("materia_exclusiva_rende_muito_dinheiro" + id_unico)
        kiposcrum["materia_exclusiva_rende_muito_dinheiro" + id_unico].Nome.append("materia_exclusiva_rende_muito_dinheiro")

        kiposcrum["DO__Disadvantage"]("arquivamento_nao_da_rendimento" + id_unico)
        kiposcrum["arquivamento_nao_da_rendimento" + id_unico].Nome.append("arquivamento_nao_da_rendimento")

        kiposcrum["DO__Alternative"]("arquivar_materia_jornalista2" + id_unico)
        kiposcrum["arquivar_materia_jornalista2" + id_unico].Nome.append("arquivar_materia_jornalista2")

        kiposcrum["DO__Risk"]("desagradar_stakeholder" + id_unico)
        kiposcrum["desagradar_stakeholder" + id_unico].Nome.append("desagradar_stakeholder")

        kiposcrum["DO__Risk"]("processo_judicial" + id_unico)
        kiposcrum["processo_judicial" + id_unico].Nome.append("processo_judicial")

        # -------------------------------

        kiposcrum["DO__Discarded_Alternative"]("arquivar_materia_jornalista2" + id_unico + "1")
        kiposcrum["arquivar_materia_jornalista2" + id_unico + "1"].Nome.append("arquivar_materia_jornalista2")

        kiposcrum["DO__Chosen_Alternative"]("publicar_materia_jornalista_2" + id_unico + "1")
        kiposcrum["publicar_materia_jornalista_2" + id_unico + "1"].Nome.append("publicar_materia_jornalista_2")

        # -------------------------------
        # -------------------------------
        # tcc_casodeestudo_KIPO_decidirmateria.png
        # relacionamentos

        kiposcrum["resolver_impasse_rapidamente" + id_unico].used_intention.append(kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico])

        kiposcrum["necessidade_de_pagar_contas_na_redacao_jornalistica" + id_unico].becomes.append(kiposcrum["resolver_impasse_rapidamente" + id_unico])
        kiposcrum["necessidade_de_pagar_contas_na_redacao_jornalistica" + id_unico].belongs_to.append(kiposcrum["gerente1" + id_unico])

        kiposcrum["gerente1" + id_unico].undertakes_to_carry_out.append(kiposcrum["resolver_impasse_rapidamente" + id_unico])
        kiposcrum["gerente1" + id_unico].undertakes_to_carry_out.append(kiposcrum["gerar_renda_para_redacao_jornalistica" + id_unico])
        kiposcrum["gerente1" + id_unico].encerrar_atividades.append(kiposcrum["final_terceiro_trimestre_2021" + id_unico])


        kiposcrum["materias_boas_sempre_devem_ser_publicadas" + id_unico].belongs_to.append(kiposcrum["gerente1" + id_unico])
        kiposcrum["materias_boas_sempre_devem_ser_publicadas" + id_unico].is_motivated_by.append(kiposcrum["necessidade_de_pagar_contas_na_redacao_jornalistica" + id_unico])
        kiposcrum["materias_boas_sempre_devem_ser_publicadas" + id_unico].is_motivated_by.append(kiposcrum["ate_agora_nenhum_risco_justificou_nao_publicar_boa_materia" + id_unico])

        kiposcrum["liberdade_de_expressao_deve_ser_pilar_central_do_trabalho" + id_unico].belongs_to.append(kiposcrum["gerente1" + id_unico])

        kiposcrum["gerente1" + id_unico].has_action.append(kiposcrum["definir_materia" + id_unico])

        kiposcrum["definir_materia" + id_unico].uses_action.append(kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico])
        kiposcrum["definir_materia" + id_unico].propositional_content_of.append(kiposcrum["a_materia_polemica_do_jornalista2_deveria_ser_publicada?" + id_unico])

        # -------------------------------


        kiposcrum["representante_investidores" + id_unico].identifies.append(kiposcrum["a_materia_polemica_do_jornalista2_deveria_ser_publicada?" + id_unico])

        kiposcrum["materia_que_desagrada_grupo_pode_ser_prejudicial" + id_unico].belongs_to.append(kiposcrum["representante_investidores" + id_unico])
        kiposcrum["materia_que_desagrada_grupo_pode_ser_prejudicial" + id_unico].is_motivated_by.append(kiposcrum["patrocinios_foram_perdidos_antes_por_conta_de_atritos_semelhantes" + id_unico])

        kiposcrum["uma_materia_muito_polemica_afeta_reputacao_do_jornal_no_longo_prazo" + id_unico].belongs_to.append(kiposcrum["representante_investidores" + id_unico])

        kiposcrum["experiencia_negativa_com_jornalista2" + id_unico].belongs_to.append(kiposcrum["representante_investidores" + id_unico])
        kiposcrum["experiencia_negativa_com_jornalista2" + id_unico].influences.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])
        # -------------------------------

        kiposcrum["tarefas_final_terceiro_trimestre_2021_dia_28_09_2021" + id_unico].ontoscrum__performs.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])

        kiposcrum["decidir_materia_destaque_setembro" + id_unico].considers.append(kiposcrum["apenas_se_publica_bom_jornalismo" + id_unico])
        kiposcrum["decidir_materia_destaque_setembro" + id_unico].considers.append(kiposcrum["um_processo_judicial_deve_ser_evitado_por_ocupar_tempo" + id_unico])
        kiposcrum["decidir_materia_destaque_setembro" + id_unico].StatusItemResolvido.append( 1 )

        # -------------------------------

        kiposcrum["risco_de_perder_relevancia_por_desperdicar_oportunidade_de_engajamento" + id_unico].threatens.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])
        kiposcrum["risco_de_perder_relevancia_por_desperdicar_oportunidade_de_engajamento" + id_unico].propositional_content_of.append(kiposcrum["arquivar_materia_jornalista2" + id_unico])

        kiposcrum["risco_de_desagradar_grupos_relevantes_por_assunto_da_noticia" + id_unico].threatens.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])
        kiposcrum["risco_de_desagradar_grupos_relevantes_por_assunto_da_noticia" + id_unico].propositional_content_of.append(kiposcrum["publicar_materia_jornalista_2" + id_unico])

        # -------------------------------

        kiposcrum["decidir_materia_destaque_setembro" + id_unico].pos_state.append(kiposcrum["publicar_materia_jornalista_2" + id_unico])
        kiposcrum["decidir_materia_destaque_setembro" + id_unico].pos_state.append(kiposcrum["arquivar_materia_jornalista2" + id_unico])
        kiposcrum["decidir_materia_destaque_setembro" + id_unico].pos_state.append(kiposcrum["arquivar_materia_jornalista2" + id_unico + "1"])
        kiposcrum["decidir_materia_destaque_setembro" + id_unico].pos_state.append(kiposcrum["publicar_materia_jornalista_2" + id_unico + "1"])

        kiposcrum["arquivamento_nao_da_rendimento" + id_unico].according_to.append(kiposcrum["engajamento" + id_unico])
        kiposcrum["arquivamento_nao_da_rendimento" + id_unico].propositional_content_of.append(kiposcrum["arquivar_materia_jornalista2" + id_unico])

        kiposcrum["materia_exclusiva_rende_muito_dinheiro" + id_unico].according_to.append(kiposcrum["engajamento" + id_unico])
        kiposcrum["materia_exclusiva_rende_muito_dinheiro" + id_unico].propositional_content_of.append(kiposcrum["publicar_materia_jornalista_2" + id_unico])

        kiposcrum["materia_polemica_por_se_tratar_de_algo_que_desfavorece_um_grupo" + id_unico].according_to.append(kiposcrum["riscos_legais" + id_unico])
        kiposcrum["materia_polemica_por_se_tratar_de_algo_que_desfavorece_um_grupo" + id_unico].propositional_content_of.append(kiposcrum["publicar_materia_jornalista_2" + id_unico])

        kiposcrum["corte_de_gastos_em_caso_de_processo" + id_unico].according_to.append(kiposcrum["riscos_legais" + id_unico])
        kiposcrum["corte_de_gastos_em_caso_de_processo" + id_unico].propositional_content_of.append(kiposcrum["arquivar_materia_jornalista2" + id_unico])

        kiposcrum["jornalista2" + id_unico].proposes.append(kiposcrum["publicar_materia_jornalista_2" + id_unico])
        kiposcrum["representante_investidores" + id_unico].proposes.append(kiposcrum["arquivar_materia_jornalista2" + id_unico])

        kiposcrum["arquivar_materia_jornalista2" + id_unico + "1"].uses.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])
        kiposcrum["arquivar_materia_jornalista2" + id_unico].uses.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])
        kiposcrum["publicar_materia_jornalista_2" + id_unico + "1"].uses.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])
        kiposcrum["publicar_materia_jornalista_2" + id_unico].uses.append(kiposcrum["backlog_de_desenvolvimento_redacao_jornalista_2021" + id_unico])

        kiposcrum["processo_judicial" + id_unico].propositional_content_of.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])
        kiposcrum["desagradar_stakeholder" + id_unico].propositional_content_of.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])

        kiposcrum["publicar_materia_jornalista_2" + id_unico + "1"].composes.append(kiposcrum["decidir_materia_destaque_setembro" + id_unico])

        # -------------------------------

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

if __name__ == '__main__':

    # contabiliza o tempo de execução!
    inicio = time.time()
    main()
    fim = time.time()

    duracao = (fim - inicio)/60
    print("\n\n\nFim da execução!\n\nDuração da execução deste script: %f minutos." % (duracao) + "\n\n")
