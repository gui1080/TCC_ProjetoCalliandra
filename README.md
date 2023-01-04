# Sistema Calliandra

Módulo de workflow com anotação semântica em Django. Implementação da [Knowledge Intensive Ontology][KIPO] com [Ontologia de Scrum][SCRUM] em caso de estudo.

Feito como parte de Projeto de Conclusão de Curso por Guilherme Braga Pinto

Para rodar localmente o sistema, execute:

> python3 manage.py runserver

Para criar ambiente virtual de Python3, execute:

> python3 -m venv venv

## Super user para admin

guilherme_teste
teste@gmail.com
12345

## Dependências

O script *./dependencias.sh* baixa dependências e executa o programa. 

Para dar permissão para rodar o script, execute:

> chmod +x dependencias.sh

Para verificar as permissões do script de dependências, execute:

> ls -l dependencias.sh

Para rodar, execute:

> python3 -m venv venv
> source venv/bin/activate
> ./dependencias.sh

Para atualizar models/forms:

> python3 manage.py makemigrations
> python3 manage.py migrate

Para gerar arquivos de requisitos:

> pip3 freeze > requirements.txt 

Para instalar o que veio no arquivo de requisitos:

> pip3 install -r requirements.txt

## Requisitos

- Python (v3.9.10)
- Django
- [OwlReady2][readthedocs]
- django-crispy-form

## Visualização da Árvore de Arquivos

````

placeholder

````

## Content Mapping do Sistema Calliandra

(último update: 24/07/2022)

![Img](https://github.com/gui1080/TCC_ProjetoCalliandra/blob/master/Midia%20Externa/content_mapping.png)

## Sobre

A Calliandra (*Calliandra dysantha Benth*) é típicamente conhecida como a flor símbolo do Cerrado, de flores vermelhas e delicadas. Ela tem uso medicinal popular, é uma planta amplamente usada para paisagismo. O Cerrado é reconhecido como a savana com maior biodiversidade do mundo, apesar de muitas espécies estarem ameaçadas de extinção.


[KIPO]: "https://www.researchgate.net/publication/282939286_KIPO_the_knowledge-intensive_process_ontology"

[SCRUM]: "https://www.researchgate.net/publication/260480541_Integration_of_classical_and_agile_project_management_methodologies_based_on_ontological_models"

[readthedocs]: "https://owlready2.readthedocs.io/en/v0.37/#"
