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

## Alterações para rodar no Servidor

Rodando com comando:

> python3 manage.py runserver 0.0.0.0:8081

### Mudar os hrefs

Os hrefs foram de href="/kipo_playground/" para href="app1/kipo_playground/". 

### settings.py

````

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'kipo_playground/staticfiles')
]

````

### views.py

````

  # No final do documento
  #-----------------------------------------------

  def show_styles_css(request):
      with open('staticfiles/css/styles.css', 'r') as f:
          data = f.read()

      response = HttpResponse(data, content_type='text/css') 
      response['Content-Disposition'] = 'attachment; filename=styles.css'
      return response

  def show_scripts_js(request):
      with open('staticfiles/js/scripts.js', 'r') as f:
          data = f.read()

      response = HttpResponse(data, content_type='text/javascript')
      response['Content-Disposition'] = 'attachment; filename=scripts.js'
      return response

  def show_ckeditor_int(request):
       with open('staticfiles/ckeditor/ckeditor-init.js', 'r') as f:
          data = f.read()

       response = HttpResponse(data, content_type='text/javascript')
       response['Content-Disposition'] = 'attachment; filename=ckeditor-init.js'
       return response

  def show_ckeditor(request):
       with open('staticfiles/ckeditor/ckeditor/ckeditor.js', 'r') as f:
          data = f.read()

       response = HttpResponse(data, content_type='text/javascript')
       response['Content-Disposition'] = 'attachment; filename=ckeditor.js'
       return response

    # Imagens

  def show_scrum_img(request):
       img = open('staticfiles/assets/scrum_img.png', 'rb')

       response = FileResponse(img)
       return response

  def show_img0132(request):
       img = open('staticfiles/assets/!IMG_0132.jpg', 'rb')

       response = FileResponse(img)
       return response

  def show_img0140(request):
       img = open('staticfiles/assets/IMG_0140.jpg', 'rb')

       response = FileResponse(img)
       return response
      
  #-----------------------------------------------

````

### urls.py

````

  # para rodar no servidor (alguns assets)
  path('static/css/styles.css', views.show_styles_css),
  path('static/js/scripts.js', views.show_scripts_js),
  #path('static/ckeditor/ckeditor/ckeditor.js', views.show_ckeditor),
  #path('static/ckeditor/ckeditor-init.js', views.show_ckeditor_init),

  path('static/assets/scrum_img.png', views.show_scrum_img),
  path('static/assets/!IMG_0132.jpg', views.show_img0132),
  path('static/assets/IMG_0140.jpg', views.show_img0140),


````

## Visualização da Árvore de Arquivos

````

.
├── .git
│   ├── branches
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── refs
│   │   │   ├── heads
│   │   │   │   └── master
│   │   │   └── remotes
│   │   │       └── origin
│   │   │           ├── HEAD
│   │   │           └── master
│   │   └── HEAD
│   ├── objects
│   │   ├── 01
│   │   │   └── a3e74bcd7a36f8e6739b8f0151e828b43642b3
│   │   ├── 0d
│   │   │   └── deb6758d30b6f236f5231338a17e3404ea496e
│   │   ├── 13
│   │   │   └── 65847b88f134c28f5144ad822731101118ee09
│   │   ├── 17
│   │   │   └── c157d6ea363253120751e14cfd9220b0f5d10a
│   │   ├── 1a
│   │   │   └── 75ff5d7be56119d79c760061531bd062ecbc77
│   │   ├── 22
│   │   │   └── b25ac6d5744265f07c2a0956abdf3c768480b8
│   │   ├── 24
│   │   │   └── 8d98a6f477b09155b32b7d698ebd5bea2d4582
│   │   ├── 26
│   │   │   └── c9f2d0098f33cf74ee6b4804393ddf5129f734
│   │   ├── 2a
│   │   │   └── 43a72052afd829b2db3437395d35ef0885e77a
│   │   ├── 2e
│   │   │   └── 1b5051f548479e250469bb113caab22f988f69
│   │   ├── 31
│   │   │   └── 9ca7a09caf4352f51edf64aafaf9e838b78d55
│   │   ├── 33
│   │   │   └── 7001426b92d359d6398eb254d9a5532d040349
│   │   ├── 37
│   │   │   └── acb63980c6d0172281fc4cfbd15c5a030f7a6e
│   │   ├── 42
│   │   │   └── 0fe053599a540deddb51e9557721b360be97ce
│   │   ├── 46
│   │   │   └── f3b5aa3c84048bf32efbd7c70db7659eddb8ed
│   │   ├── 48
│   │   │   └── 2ad57685f2f75d9d08049bc8cc52bf74e9f286
│   │   ├── 53
│   │   │   └── 2b2a0afb57dbe4771d99761805f34bfab7e7c2
│   │   ├── 56
│   │   │   ├── abdc8bd265266fc5a525b68cbe9585c7484aeb
│   │   │   ├── b0fe006fa47fa2a7d96f5a682718e362424cf8
│   │   │   └── c6558cd4eefb945f87708aef7106a4484fa05b
│   │   ├── 87
│   │   │   ├── 0a70c03ad311ebbc49a77592cde81232676a7c
│   │   │   └── 590fc39c310dee10aa452a20690dc7ef46a31f
│   │   ├── a0
│   │   │   └── 1be3d842ce6f23fecb24a1392554f9d9fcdba4
│   │   ├── a7
│   │   │   └── d0d99f49e8d8646f9926a93fbbaa0b1b447465
│   │   ├── aa
│   │   │   └── 3c5bad5a90904521b5a4a9783ef3345b2e28b8
│   │   ├── ac
│   │   │   └── 0bd7968d7f40f1f12df3278aeaa40828911f5a
│   │   ├── b3
│   │   │   └── 33ab97458aadff59a0f58d9de66f15004b6049
│   │   ├── ba
│   │   │   └── 13fc70220807091911d090c47fe47c51039260
│   │   ├── d6
│   │   │   └── c916e5e1bd9677cc7066990e34ecc4abe6a74f
│   │   ├── df
│   │   │   └── 950872f1a3ae1e273fe4aea2d426e1d84af557
│   │   ├── e0
│   │   │   └── d0f49dbe2e82fdb1ea10ecbaf0efe1de4c62b3
│   │   ├── e7
│   │   │   └── 6b58f61aebacf6914255cd0c17e4f9fb8751c8
│   │   ├── e8
│   │   │   └── 73fe0a2db720083842d637175edf95e78e2d5d
│   │   ├── e9
│   │   │   └── 8681cf69f14fa8030d2663e02d879320388d9e
│   │   ├── fb
│   │   │   └── f3106f71515c4908ed8b37e01fbeb03dce9c8e
│   │   ├── info
│   │   └── pack
│   │       ├── pack-7279f91a0fb2bc32f23443b35f24ae96d1813368.idx
│   │       └── pack-7279f91a0fb2bc32f23443b35f24ae96d1813368.pack
│   ├── refs
│   │   ├── heads
│   │   │   └── master
│   │   ├── remotes
│   │   │   └── origin
│   │   │       ├── HEAD
│   │   │       └── master
│   │   └── tags
│   ├── COMMIT_EDITMSG
│   ├── config
│   ├── description
│   ├── FETCH_HEAD
│   ├── HEAD
│   ├── index
│   ├── ORIG_HEAD
│   └── packed-refs
├── kipo_playground
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-310.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── forms.cpython-39.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-39.pyc
│   │   ├── views.cpython-310.pyc
│   │   └── views.cpython-39.pyc
│   ├── migrations
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── 0001_initial.cpython-310.pyc
│   │   │   └── 0002_materiajornalistica_data_atualizacao_and_more.cpython-310.pyc
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_materiajornalistica_data_atualizacao_and_more.py
│   ├── static
│   │   ├── assets
│   │   │   ├── !IMG_0132.jpg
│   │   │   ├── decisao_site.png
│   │   │   ├── favicon.ico
│   │   │   ├── icon.ico
│   │   │   ├── IMG_0140.jpg
│   │   │   └── scrum_img.png
│   │   ├── css
│   │   │   └── styles.css
│   │   ├── js
│   │   │   └── scripts.js
│   │   └── .DS_Store
│   ├── templates
│   │   ├── alocar_pessoas.html
│   │   ├── artefatos_alocar_dashboard.html
│   │   ├── artefatos_dashboard.html
│   │   ├── backlog_item_status.html
│   │   ├── backlog_produto.html
│   │   ├── backlog_sprint.html
│   │   ├── comentario_artefato.html
│   │   ├── daily_dashboard.html
│   │   ├── decision_dashboard.html
│   │   ├── deletar_instancias.html
│   │   ├── escolher_instancia_previa.html
│   │   ├── gestao_pessoas.html
│   │   ├── inserir_instancia_tela_ok.html
│   │   ├── inserir_obs_tela_ok.html
│   │   ├── inserir_relacao_tela_ok.html
│   │   ├── instancia_previa_tela_ok.html
│   │   ├── instancias_inserir_select.html
│   │   ├── instancias_tipo_select.html
│   │   ├── instancias_tipo_show.html
│   │   ├── instancias.html
│   │   ├── item_inserir_esforco.html
│   │   ├── item_inserir_obs.html
│   │   ├── ler_materia.html
│   │   ├── nova_materia.html
│   │   ├── seleciona_decisao.html
│   │   ├── seleciona_sprint.html
│   │   ├── sobre.html
│   │   ├── sprint_dashboard.html
│   │   ├── sprint_options.html
│   │   ├── tutorial.html
│   │   ├── ver_materia.html
│   │   ├── welcome_graficos.html
│   │   └── welcome.html
│   ├── __init__.py
│   ├── .DS_Store
│   ├── admin.py
│   ├── apps.py
│   ├── db.sqlite3
│   ├── forms.py
│   ├── kipo_fialho.owl
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Midia Externa
│   ├── Scripts de Inicialização do BD
│   │   ├── Diagramas DrawIo
│   │   │   ├── equivalencia.drawio
│   │   │   ├── equivalencia.png
│   │   │   ├── PMBOK_ontology.drawio
│   │   │   ├── Scrum_Ontology_Alto_Nivel.drawio
│   │   │   ├── Scrum_Ontology_Alto_Nivel.drawio.png
│   │   │   ├── Scrum_ontology.drawio
│   │   │   ├── Scrum_ontology.png
│   │   │   ├── tcc_casodeestudo_KIPO.drawio
│   │   │   ├── tcc_casodeestudo_KIPO.drawio.png
│   │   │   ├── tcc_casodeestudo.drawio
│   │   │   └── tcc_casodeestudo.drawio.png
│   │   ├── .DS_Store
│   │   ├── backup.db
│   │   ├── fact_check.py
│   │   ├── kipo_fialho.owl
│   │   ├── kiposcrum_pellet.owl
│   │   ├── kiposcrum_pellet2.owl
│   │   └── main.py
│   ├── Scripts de Inicialização do BD - Jornalismo
│   │   ├── backup.db
│   │   ├── kipo_fialho.owl
│   │   ├── main.py
│   │   ├── tcc_casodeestudo_jornalismo.drawio
│   │   ├── tcc_casodeestudo_jornalismo.png
│   │   ├── tcc_casodeestudo_KIPO_BD.drawio
│   │   ├── tcc_casodeestudo_KIPO_BD.png
│   │   ├── tcc_casodeestudo_KIPO_decidirmateria.drawio
│   │   └── tcc_casodeestudo_KIPO_decidirmateria.png
│   ├── .$content_mapping.drawio.bkp
│   ├── .DS_Store
│   ├── adição no sistema.drawio
│   ├── adição no sistema.png
│   ├── adição no sistema.png
│   ├── arquitetura.drawio
│   ├── arquitetura.png
│   ├── bd_owl2ready.png
│   ├── content_mapping.drawio
│   ├── content_mapping.png
│   ├── decisao_qualquer.drawio
│   ├── decisao_qualquer.png
│   ├── decisao_site.drawio
│   ├── decisao_site.png
│   ├── equivalencia.drawio
│   ├── equivalencia.png
│   ├── kipo_resumo.drawio
│   ├── kipo_resumo.png
│   ├── navio.drawio
│   ├── navio.png
│   ├── scrum_img.drawio
│   ├── scrum_img.png
│   ├── Scrum_Ontology_Alto_Nivel.drawio
│   ├── Scrum_Ontology_Alto_Nivel.png
│   ├── triplas.drawio
│   └── triplas.png
├── staticfiles
│   ├── admin
│   │   ├── css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │       ├── select2.css
│   │   │   │       └── select2.min.css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dark_mode.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── nav_sidebar.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── responsive.css
│   │   │   ├── rtl.css
│   │   │   └── widgets.css
│   │   ├── fonts
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img
│   │   │   ├── gis
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── calendar-icons.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   └── js
│   │       ├── admin
│   │       │   ├── DateTimeShortcuts.js
│   │       │   └── RelatedObjectLookups.js
│   │       ├── vendor
│   │       │   ├── jquery
│   │       │   │   ├── jquery.js
│   │       │   │   ├── jquery.min.js
│   │       │   │   └── LICENSE.txt
│   │       │   ├── select2
│   │       │   │   ├── i18n
│   │       │   │   │   ├── af.js
│   │       │   │   │   ├── ar.js
│   │       │   │   │   ├── az.js
│   │       │   │   │   ├── bg.js
│   │       │   │   │   ├── bn.js
│   │       │   │   │   ├── bs.js
│   │       │   │   │   ├── ca.js
│   │       │   │   │   ├── cs.js
│   │       │   │   │   ├── da.js
│   │       │   │   │   ├── de.js
│   │       │   │   │   ├── dsb.js
│   │       │   │   │   ├── el.js
│   │       │   │   │   ├── en.js
│   │       │   │   │   ├── es.js
│   │       │   │   │   ├── et.js
│   │       │   │   │   ├── eu.js
│   │       │   │   │   ├── fa.js
│   │       │   │   │   ├── fi.js
│   │       │   │   │   ├── fr.js
│   │       │   │   │   ├── gl.js
│   │       │   │   │   ├── he.js
│   │       │   │   │   ├── hi.js
│   │       │   │   │   ├── hr.js
│   │       │   │   │   ├── hsb.js
│   │       │   │   │   ├── hu.js
│   │       │   │   │   ├── hy.js
│   │       │   │   │   ├── id.js
│   │       │   │   │   ├── is.js
│   │       │   │   │   ├── it.js
│   │       │   │   │   ├── ja.js
│   │       │   │   │   ├── ka.js
│   │       │   │   │   ├── km.js
│   │       │   │   │   ├── ko.js
│   │       │   │   │   ├── lt.js
│   │       │   │   │   ├── lv.js
│   │       │   │   │   ├── mk.js
│   │       │   │   │   ├── ms.js
│   │       │   │   │   ├── nb.js
│   │       │   │   │   ├── ne.js
│   │       │   │   │   ├── nl.js
│   │       │   │   │   ├── pl.js
│   │       │   │   │   ├── ps.js
│   │       │   │   │   ├── pt-BR.js
│   │       │   │   │   ├── pt.js
│   │       │   │   │   ├── ro.js
│   │       │   │   │   ├── ru.js
│   │       │   │   │   ├── sk.js
│   │       │   │   │   ├── sl.js
│   │       │   │   │   ├── sq.js
│   │       │   │   │   ├── sr-Cyrl.js
│   │       │   │   │   ├── sr.js
│   │       │   │   │   ├── sv.js
│   │       │   │   │   ├── th.js
│   │       │   │   │   ├── tk.js
│   │       │   │   │   ├── tr.js
│   │       │   │   │   ├── uk.js
│   │       │   │   │   ├── vi.js
│   │       │   │   │   ├── zh-CN.js
│   │       │   │   │   └── zh-TW.js
│   │       │   │   ├── LICENSE.md
│   │       │   │   ├── select2.full.js
│   │       │   │   └── select2.full.min.js
│   │       │   └── xregexp
│   │       │       ├── LICENSE.txt
│   │       │       ├── xregexp.js
│   │       │       └── xregexp.min.js
│   │       ├── actions.js
│   │       ├── autocomplete.js
│   │       ├── calendar.js
│   │       ├── cancel.js
│   │       ├── change_form.js
│   │       ├── collapse.js
│   │       ├── core.js
│   │       ├── filters.js
│   │       ├── inlines.js
│   │       ├── jquery.init.js
│   │       ├── nav_sidebar.js
│   │       ├── popup_response.js
│   │       ├── prepopulate_init.js
│   │       ├── prepopulate.js
│   │       ├── SelectBox.js
│   │       ├── SelectFilter2.js
│   │       └── urlify.js
│   ├── assets
│   │   ├── !IMG_0132.jpg
│   │   ├── decisao_site.png
│   │   ├── favicon.ico
│   │   ├── icon.ico
│   │   ├── IMG_0140.jpg
│   │   └── scrum_img.png
│   ├── ckeditor
│   │   ├── ckeditor
│   │   │   ├── adapters
│   │   │   │   └── jquery.js
│   │   │   ├── lang
│   │   │   │   ├── af.js
│   │   │   │   ├── ar.js
│   │   │   │   ├── az.js
│   │   │   │   ├── bg.js
│   │   │   │   ├── bn.js
│   │   │   │   ├── bs.js
│   │   │   │   ├── ca.js
│   │   │   │   ├── cs.js
│   │   │   │   ├── cy.js
│   │   │   │   ├── da.js
│   │   │   │   ├── de-ch.js
│   │   │   │   ├── de.js
│   │   │   │   ├── el.js
│   │   │   │   ├── en-au.js
│   │   │   │   ├── en-ca.js
│   │   │   │   ├── en-gb.js
│   │   │   │   ├── en.js
│   │   │   │   ├── eo.js
│   │   │   │   ├── es-mx.js
│   │   │   │   ├── es.js
│   │   │   │   ├── et.js
│   │   │   │   ├── eu.js
│   │   │   │   ├── fa.js
│   │   │   │   ├── fi.js
│   │   │   │   ├── fo.js
│   │   │   │   ├── fr-ca.js
│   │   │   │   ├── fr.js
│   │   │   │   ├── gl.js
│   │   │   │   ├── gu.js
│   │   │   │   ├── he.js
│   │   │   │   ├── hi.js
│   │   │   │   ├── hr.js
│   │   │   │   ├── hu.js
│   │   │   │   ├── id.js
│   │   │   │   ├── is.js
│   │   │   │   ├── it.js
│   │   │   │   ├── ja.js
│   │   │   │   ├── ka.js
│   │   │   │   ├── km.js
│   │   │   │   ├── ko.js
│   │   │   │   ├── ku.js
│   │   │   │   ├── lt.js
│   │   │   │   ├── lv.js
│   │   │   │   ├── mk.js
│   │   │   │   ├── mn.js
│   │   │   │   ├── ms.js
│   │   │   │   ├── nb.js
│   │   │   │   ├── nl.js
│   │   │   │   ├── no.js
│   │   │   │   ├── oc.js
│   │   │   │   ├── pl.js
│   │   │   │   ├── pt-br.js
│   │   │   │   ├── pt.js
│   │   │   │   ├── ro.js
│   │   │   │   ├── ru.js
│   │   │   │   ├── si.js
│   │   │   │   ├── sk.js
│   │   │   │   ├── sl.js
│   │   │   │   ├── sq.js
│   │   │   │   ├── sr-latn.js
│   │   │   │   ├── sr.js
│   │   │   │   ├── sv.js
│   │   │   │   ├── th.js
│   │   │   │   ├── tr.js
│   │   │   │   ├── tt.js
│   │   │   │   ├── ug.js
│   │   │   │   ├── uk.js
│   │   │   │   ├── vi.js
│   │   │   │   ├── zh-cn.js
│   │   │   │   └── zh.js
│   │   │   ├── plugins
│   │   │   │   ├── a11yhelp
│   │   │   │   │   └── dialogs
│   │   │   │   │       ├── lang
│   │   │   │   │       │   ├── _translationstatus.txt
│   │   │   │   │       │   ├── af.js
│   │   │   │   │       │   ├── ar.js
│   │   │   │   │       │   ├── az.js
│   │   │   │   │       │   ├── bg.js
│   │   │   │   │       │   ├── ca.js
│   │   │   │   │       │   ├── cs.js
│   │   │   │   │       │   ├── cy.js
│   │   │   │   │       │   ├── da.js
│   │   │   │   │       │   ├── de-ch.js
│   │   │   │   │       │   ├── de.js
│   │   │   │   │       │   ├── el.js
│   │   │   │   │       │   ├── en-au.js
│   │   │   │   │       │   ├── en-gb.js
│   │   │   │   │       │   ├── en.js
│   │   │   │   │       │   ├── eo.js
│   │   │   │   │       │   ├── es-mx.js
│   │   │   │   │       │   ├── es.js
│   │   │   │   │       │   ├── et.js
│   │   │   │   │       │   ├── eu.js
│   │   │   │   │       │   ├── fa.js
│   │   │   │   │       │   ├── fi.js
│   │   │   │   │       │   ├── fo.js
│   │   │   │   │       │   ├── fr-ca.js
│   │   │   │   │       │   ├── fr.js
│   │   │   │   │       │   ├── gl.js
│   │   │   │   │       │   ├── gu.js
│   │   │   │   │       │   ├── he.js
│   │   │   │   │       │   ├── hi.js
│   │   │   │   │       │   ├── hr.js
│   │   │   │   │       │   ├── hu.js
│   │   │   │   │       │   ├── id.js
│   │   │   │   │       │   ├── it.js
│   │   │   │   │       │   ├── ja.js
│   │   │   │   │       │   ├── km.js
│   │   │   │   │       │   ├── ko.js
│   │   │   │   │       │   ├── ku.js
│   │   │   │   │       │   ├── lt.js
│   │   │   │   │       │   ├── lv.js
│   │   │   │   │       │   ├── mk.js
│   │   │   │   │       │   ├── mn.js
│   │   │   │   │       │   ├── nb.js
│   │   │   │   │       │   ├── nl.js
│   │   │   │   │       │   ├── no.js
│   │   │   │   │       │   ├── oc.js
│   │   │   │   │       │   ├── pl.js
│   │   │   │   │       │   ├── pt-br.js
│   │   │   │   │       │   ├── pt.js
│   │   │   │   │       │   ├── ro.js
│   │   │   │   │       │   ├── ru.js
│   │   │   │   │       │   ├── si.js
│   │   │   │   │       │   ├── sk.js
│   │   │   │   │       │   ├── sl.js
│   │   │   │   │       │   ├── sq.js
│   │   │   │   │       │   ├── sr-latn.js
│   │   │   │   │       │   ├── sr.js
│   │   │   │   │       │   ├── sv.js
│   │   │   │   │       │   ├── th.js
│   │   │   │   │       │   ├── tr.js
│   │   │   │   │       │   ├── tt.js
│   │   │   │   │       │   ├── ug.js
│   │   │   │   │       │   ├── uk.js
│   │   │   │   │       │   ├── vi.js
│   │   │   │   │       │   ├── zh-cn.js
│   │   │   │   │       │   └── zh.js
│   │   │   │   │       └── a11yhelp.js
│   │   │   │   ├── about
│   │   │   │   │   └── dialogs
│   │   │   │   │       ├── hidpi
│   │   │   │   │       │   └── logo_ckeditor.png
│   │   │   │   │       ├── about.js
│   │   │   │   │       └── logo_ckeditor.png
│   │   │   │   ├── adobeair
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── ajax
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── autoembed
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── autogrow
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── autolink
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── bbcode
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── clipboard
│   │   │   │   │   └── dialogs
│   │   │   │   │       └── paste.js
│   │   │   │   ├── codesnippet
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── codesnippet.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── codesnippet.png
│   │   │   │   │   │   └── codesnippet.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   ├── lib
│   │   │   │   │   │   └── highlight
│   │   │   │   │   │       ├── styles
│   │   │   │   │   │       │   ├── arta.css
│   │   │   │   │   │       │   ├── ascetic.css
│   │   │   │   │   │       │   ├── atelier-dune.dark.css
│   │   │   │   │   │       │   ├── atelier-dune.light.css
│   │   │   │   │   │       │   ├── atelier-forest.dark.css
│   │   │   │   │   │       │   ├── atelier-forest.light.css
│   │   │   │   │   │       │   ├── atelier-heath.dark.css
│   │   │   │   │   │       │   ├── atelier-heath.light.css
│   │   │   │   │   │       │   ├── atelier-lakeside.dark.css
│   │   │   │   │   │       │   ├── atelier-lakeside.light.css
│   │   │   │   │   │       │   ├── atelier-seaside.dark.css
│   │   │   │   │   │       │   ├── atelier-seaside.light.css
│   │   │   │   │   │       │   ├── brown_paper.css
│   │   │   │   │   │       │   ├── brown_papersq.png
│   │   │   │   │   │       │   ├── dark.css
│   │   │   │   │   │       │   ├── default.css
│   │   │   │   │   │       │   ├── docco.css
│   │   │   │   │   │       │   ├── far.css
│   │   │   │   │   │       │   ├── foundation.css
│   │   │   │   │   │       │   ├── github.css
│   │   │   │   │   │       │   ├── googlecode.css
│   │   │   │   │   │       │   ├── idea.css
│   │   │   │   │   │       │   ├── ir_black.css
│   │   │   │   │   │       │   ├── magula.css
│   │   │   │   │   │       │   ├── mono-blue.css
│   │   │   │   │   │       │   ├── monokai_sublime.css
│   │   │   │   │   │       │   ├── monokai.css
│   │   │   │   │   │       │   ├── obsidian.css
│   │   │   │   │   │       │   ├── paraiso.dark.css
│   │   │   │   │   │       │   ├── paraiso.light.css
│   │   │   │   │   │       │   ├── pojoaque.css
│   │   │   │   │   │       │   ├── pojoaque.jpg
│   │   │   │   │   │       │   ├── railscasts.css
│   │   │   │   │   │       │   ├── rainbow.css
│   │   │   │   │   │       │   ├── school_book.css
│   │   │   │   │   │       │   ├── school_book.png
│   │   │   │   │   │       │   ├── solarized_dark.css
│   │   │   │   │   │       │   ├── solarized_light.css
│   │   │   │   │   │       │   ├── sunburst.css
│   │   │   │   │   │       │   ├── tomorrow-night-blue.css
│   │   │   │   │   │       │   ├── tomorrow-night-bright.css
│   │   │   │   │   │       │   ├── tomorrow-night-eighties.css
│   │   │   │   │   │       │   ├── tomorrow-night.css
│   │   │   │   │   │       │   ├── tomorrow.css
│   │   │   │   │   │       │   ├── vs.css
│   │   │   │   │   │       │   ├── xcode.css
│   │   │   │   │   │       │   └── zenburn.css
│   │   │   │   │   │       ├── CHANGES.md
│   │   │   │   │   │       ├── highlight.pack.js
│   │   │   │   │   │       ├── LICENSE
│   │   │   │   │   │       └── README.ru.md
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── codesnippetgeshi
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── colordialog
│   │   │   │   │   └── dialogs
│   │   │   │   │       ├── colordialog.css
│   │   │   │   │       └── colordialog.js
│   │   │   │   ├── copyformatting
│   │   │   │   │   ├── cursors
│   │   │   │   │   │   ├── cursor-disabled.svg
│   │   │   │   │   │   └── cursor.svg
│   │   │   │   │   └── styles
│   │   │   │   │       └── copyformatting.css
│   │   │   │   ├── devtools
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── _translationstatus.txt
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── gu.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── si.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── dialog
│   │   │   │   │   ├── styles
│   │   │   │   │   │   └── dialog.css
│   │   │   │   │   └── dialogDefinition.js
│   │   │   │   ├── div
│   │   │   │   │   └── dialogs
│   │   │   │   │       └── div.js
│   │   │   │   ├── divarea
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── docprops
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── docprops.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   ├── docprops-rtl.png
│   │   │   │   │   │   │   └── docprops.png
│   │   │   │   │   │   ├── docprops-rtl.png
│   │   │   │   │   │   └── docprops.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-au.js
│   │   │   │   │   │   ├── en-ca.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fo.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── gu.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   ├── mn.js
│   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── si.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sr-latn.js
│   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── embed
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── embed.png
│   │   │   │   │   │   └── embed.png
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── embedbase
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── embedbase.js
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── embedsemantic
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── embedsemantic.png
│   │   │   │   │   │   └── embedsemantic.png
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── exportpdf
│   │   │   │   │   ├── tests
│   │   │   │   │   │   ├── _helpers
│   │   │   │   │   │   │   └── tools.js
│   │   │   │   │   │   ├── manual
│   │   │   │   │   │   │   ├── integrations
│   │   │   │   │   │   │   │   ├── easyimage.html
│   │   │   │   │   │   │   │   └── easyimage.md
│   │   │   │   │   │   │   ├── configfilename.html
│   │   │   │   │   │   │   ├── configfilename.md
│   │   │   │   │   │   │   ├── emptyeditor.html
│   │   │   │   │   │   │   ├── emptyeditor.md
│   │   │   │   │   │   │   ├── integration.html
│   │   │   │   │   │   │   ├── integration.md
│   │   │   │   │   │   │   ├── notifications.html
│   │   │   │   │   │   │   ├── notifications.md
│   │   │   │   │   │   │   ├── notificationsasync.html
│   │   │   │   │   │   │   ├── notificationsasync.md
│   │   │   │   │   │   │   ├── paperformat.html
│   │   │   │   │   │   │   ├── paperformat.md
│   │   │   │   │   │   │   ├── readonly.html
│   │   │   │   │   │   │   ├── readonly.md
│   │   │   │   │   │   │   ├── stylesheets.html
│   │   │   │   │   │   │   ├── stylesheets.md
│   │   │   │   │   │   │   ├── tokenfetching.html
│   │   │   │   │   │   │   ├── tokenfetching.md
│   │   │   │   │   │   │   ├── tokentwoeditorscorrect.html
│   │   │   │   │   │   │   ├── tokentwoeditorscorrect.md
│   │   │   │   │   │   │   ├── tokentwoeditorswrong.html
│   │   │   │   │   │   │   ├── tokentwoeditorswrong.md
│   │   │   │   │   │   │   ├── tokenwithouturl.html
│   │   │   │   │   │   │   ├── tokenwithouturl.md
│   │   │   │   │   │   │   ├── wrongendpoint.html
│   │   │   │   │   │   │   └── wrongendpoint.md
│   │   │   │   │   │   ├── authentication.js
│   │   │   │   │   │   ├── exportpdf.js
│   │   │   │   │   │   ├── notification.js
│   │   │   │   │   │   ├── resourcespaths.js
│   │   │   │   │   │   ├── statistics.js
│   │   │   │   │   │   └── stylesheets.js
│   │   │   │   │   ├── CHANGELOG.md
│   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   ├── plugindefinition.js
│   │   │   │   │   └── README.md
│   │   │   │   ├── filetools
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── find
│   │   │   │   │   └── dialogs
│   │   │   │   │       └── find.js
│   │   │   │   ├── flash
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── flash.js
│   │   │   │   │   └── images
│   │   │   │   │       └── placeholder.png
│   │   │   │   ├── forms
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   ├── button.js
│   │   │   │   │   │   ├── checkbox.js
│   │   │   │   │   │   ├── form.js
│   │   │   │   │   │   ├── hiddenfield.js
│   │   │   │   │   │   ├── radio.js
│   │   │   │   │   │   ├── select.js
│   │   │   │   │   │   ├── textarea.js
│   │   │   │   │   │   └── textfield.js
│   │   │   │   │   └── images
│   │   │   │   │       └── hiddenfield.gif
│   │   │   │   ├── iframe
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── iframe.js
│   │   │   │   │   └── images
│   │   │   │   │       └── placeholder.png
│   │   │   │   ├── iframedialog
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── image
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── image.js
│   │   │   │   │   └── images
│   │   │   │   │       └── noimage.png
│   │   │   │   ├── image2
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── image2.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── image.png
│   │   │   │   │   │   └── image.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-au.js
│   │   │   │   │   │   ├── en-ca.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fo.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── gu.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   ├── mn.js
│   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── si.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sr-latn.js
│   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── language
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── language.png
│   │   │   │   │   │   └── language.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fo.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── lineutils
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── link
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   ├── anchor.js
│   │   │   │   │   │   └── link.js
│   │   │   │   │   └── images
│   │   │   │   │       ├── hidpi
│   │   │   │   │       │   └── anchor.png
│   │   │   │   │       └── anchor.png
│   │   │   │   ├── liststyle
│   │   │   │   │   └── dialogs
│   │   │   │   │       └── liststyle.js
│   │   │   │   ├── magicline
│   │   │   │   │   └── images
│   │   │   │   │       ├── hidpi
│   │   │   │   │       │   ├── icon-rtl.png
│   │   │   │   │       │   └── icon.png
│   │   │   │   │       ├── icon-rtl.png
│   │   │   │   │       └── icon.png
│   │   │   │   ├── mathjax
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── mathjax.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── mathjax.png
│   │   │   │   │   │   └── mathjax.png
│   │   │   │   │   ├── images
│   │   │   │   │   │   └── loader.gif
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── menubutton
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── notification
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── notificationaggregator
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── pagebreak
│   │   │   │   │   └── images
│   │   │   │   │       └── pagebreak.gif
│   │   │   │   ├── pastefromgdocs
│   │   │   │   │   └── filter
│   │   │   │   │       └── default.js
│   │   │   │   ├── pastefromlibreoffice
│   │   │   │   │   └── filter
│   │   │   │   │       └── default.js
│   │   │   │   ├── pastefromword
│   │   │   │   │   └── filter
│   │   │   │   │       └── default.js
│   │   │   │   ├── pastetools
│   │   │   │   │   └── filter
│   │   │   │   │       ├── common.js
│   │   │   │   │       └── image.js
│   │   │   │   ├── placeholder
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── placeholder.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── placeholder.png
│   │   │   │   │   │   └── placeholder.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── si.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── preview
│   │   │   │   │   ├── images
│   │   │   │   │   │   └── pagebreak.gif
│   │   │   │   │   ├── styles
│   │   │   │   │   │   └── screen.css
│   │   │   │   │   └── preview.html
│   │   │   │   ├── scayt
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   ├── dialog.css
│   │   │   │   │   │   ├── options.js
│   │   │   │   │   │   └── toolbar.css
│   │   │   │   │   ├── skins
│   │   │   │   │   │   └── moono-lisa
│   │   │   │   │   │       └── scayt.css
│   │   │   │   │   ├── CHANGELOG.md
│   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   └── README.md
│   │   │   │   ├── sharedspace
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── showblocks
│   │   │   │   │   └── images
│   │   │   │   │       ├── block_address.png
│   │   │   │   │       ├── block_blockquote.png
│   │   │   │   │       ├── block_div.png
│   │   │   │   │       ├── block_h1.png
│   │   │   │   │       ├── block_h2.png
│   │   │   │   │       ├── block_h3.png
│   │   │   │   │       ├── block_h4.png
│   │   │   │   │       ├── block_h5.png
│   │   │   │   │       ├── block_h6.png
│   │   │   │   │       ├── block_p.png
│   │   │   │   │       └── block_pre.png
│   │   │   │   ├── smiley
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── smiley.js
│   │   │   │   │   └── images
│   │   │   │   │       ├── angel_smile.gif
│   │   │   │   │       ├── angel_smile.png
│   │   │   │   │       ├── angry_smile.gif
│   │   │   │   │       ├── angry_smile.png
│   │   │   │   │       ├── broken_heart.gif
│   │   │   │   │       ├── broken_heart.png
│   │   │   │   │       ├── confused_smile.gif
│   │   │   │   │       ├── confused_smile.png
│   │   │   │   │       ├── cry_smile.gif
│   │   │   │   │       ├── cry_smile.png
│   │   │   │   │       ├── devil_smile.gif
│   │   │   │   │       ├── devil_smile.png
│   │   │   │   │       ├── embaressed_smile.gif
│   │   │   │   │       ├── embarrassed_smile.gif
│   │   │   │   │       ├── embarrassed_smile.png
│   │   │   │   │       ├── envelope.gif
│   │   │   │   │       ├── envelope.png
│   │   │   │   │       ├── heart.gif
│   │   │   │   │       ├── heart.png
│   │   │   │   │       ├── kiss.gif
│   │   │   │   │       ├── kiss.png
│   │   │   │   │       ├── lightbulb.gif
│   │   │   │   │       ├── lightbulb.png
│   │   │   │   │       ├── omg_smile.gif
│   │   │   │   │       ├── omg_smile.png
│   │   │   │   │       ├── regular_smile.gif
│   │   │   │   │       ├── regular_smile.png
│   │   │   │   │       ├── sad_smile.gif
│   │   │   │   │       ├── sad_smile.png
│   │   │   │   │       ├── shades_smile.gif
│   │   │   │   │       ├── shades_smile.png
│   │   │   │   │       ├── teeth_smile.gif
│   │   │   │   │       ├── teeth_smile.png
│   │   │   │   │       ├── thumbs_down.gif
│   │   │   │   │       ├── thumbs_down.png
│   │   │   │   │       ├── thumbs_up.gif
│   │   │   │   │       ├── thumbs_up.png
│   │   │   │   │       ├── tongue_smile.gif
│   │   │   │   │       ├── tongue_smile.png
│   │   │   │   │       ├── tounge_smile.gif
│   │   │   │   │       ├── whatchutalkingabout_smile.gif
│   │   │   │   │       ├── whatchutalkingabout_smile.png
│   │   │   │   │       ├── wink_smile.gif
│   │   │   │   │       └── wink_smile.png
│   │   │   │   ├── sourcedialog
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── sourcedialog.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   ├── sourcedialog-rtl.png
│   │   │   │   │   │   │   └── sourcedialog.png
│   │   │   │   │   │   ├── sourcedialog-rtl.png
│   │   │   │   │   │   └── sourcedialog.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-au.js
│   │   │   │   │   │   ├── en-ca.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fo.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── gu.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mn.js
│   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── si.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sr-latn.js
│   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── specialchar
│   │   │   │   │   └── dialogs
│   │   │   │   │       ├── lang
│   │   │   │   │       │   ├── _translationstatus.txt
│   │   │   │   │       │   ├── af.js
│   │   │   │   │       │   ├── ar.js
│   │   │   │   │       │   ├── az.js
│   │   │   │   │       │   ├── bg.js
│   │   │   │   │       │   ├── ca.js
│   │   │   │   │       │   ├── cs.js
│   │   │   │   │       │   ├── cy.js
│   │   │   │   │       │   ├── da.js
│   │   │   │   │       │   ├── de-ch.js
│   │   │   │   │       │   ├── de.js
│   │   │   │   │       │   ├── el.js
│   │   │   │   │       │   ├── en-au.js
│   │   │   │   │       │   ├── en-ca.js
│   │   │   │   │       │   ├── en-gb.js
│   │   │   │   │       │   ├── en.js
│   │   │   │   │       │   ├── eo.js
│   │   │   │   │       │   ├── es-mx.js
│   │   │   │   │       │   ├── es.js
│   │   │   │   │       │   ├── et.js
│   │   │   │   │       │   ├── eu.js
│   │   │   │   │       │   ├── fa.js
│   │   │   │   │       │   ├── fi.js
│   │   │   │   │       │   ├── fr-ca.js
│   │   │   │   │       │   ├── fr.js
│   │   │   │   │       │   ├── gl.js
│   │   │   │   │       │   ├── he.js
│   │   │   │   │       │   ├── hr.js
│   │   │   │   │       │   ├── hu.js
│   │   │   │   │       │   ├── id.js
│   │   │   │   │       │   ├── it.js
│   │   │   │   │       │   ├── ja.js
│   │   │   │   │       │   ├── km.js
│   │   │   │   │       │   ├── ko.js
│   │   │   │   │       │   ├── ku.js
│   │   │   │   │       │   ├── lt.js
│   │   │   │   │       │   ├── lv.js
│   │   │   │   │       │   ├── nb.js
│   │   │   │   │       │   ├── nl.js
│   │   │   │   │       │   ├── no.js
│   │   │   │   │       │   ├── oc.js
│   │   │   │   │       │   ├── pl.js
│   │   │   │   │       │   ├── pt-br.js
│   │   │   │   │       │   ├── pt.js
│   │   │   │   │       │   ├── ro.js
│   │   │   │   │       │   ├── ru.js
│   │   │   │   │       │   ├── si.js
│   │   │   │   │       │   ├── sk.js
│   │   │   │   │       │   ├── sl.js
│   │   │   │   │       │   ├── sq.js
│   │   │   │   │       │   ├── sr-latn.js
│   │   │   │   │       │   ├── sr.js
│   │   │   │   │       │   ├── sv.js
│   │   │   │   │       │   ├── th.js
│   │   │   │   │       │   ├── tr.js
│   │   │   │   │       │   ├── tt.js
│   │   │   │   │       │   ├── ug.js
│   │   │   │   │       │   ├── uk.js
│   │   │   │   │       │   ├── vi.js
│   │   │   │   │       │   ├── zh-cn.js
│   │   │   │   │       │   └── zh.js
│   │   │   │   │       └── specialchar.js
│   │   │   │   ├── stylesheetparser
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── table
│   │   │   │   │   └── dialogs
│   │   │   │   │       └── table.js
│   │   │   │   ├── tableresize
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── tableselection
│   │   │   │   │   └── styles
│   │   │   │   │       └── tableselection.css
│   │   │   │   ├── tabletools
│   │   │   │   │   └── dialogs
│   │   │   │   │       └── tableCell.js
│   │   │   │   ├── templates
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   ├── templates.css
│   │   │   │   │   │   └── templates.js
│   │   │   │   │   ├── templates
│   │   │   │   │   │   ├── images
│   │   │   │   │   │   │   ├── template1.gif
│   │   │   │   │   │   │   ├── template2.gif
│   │   │   │   │   │   │   └── template3.gif
│   │   │   │   │   │   └── default.js
│   │   │   │   │   └── templatedefinition.js
│   │   │   │   ├── uicolor
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   └── uicolor.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── uicolor.png
│   │   │   │   │   │   └── uicolor.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── _translationstatus.txt
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── si.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   ├── yui
│   │   │   │   │   │   ├── assets
│   │   │   │   │   │   │   ├── hue_bg.png
│   │   │   │   │   │   │   ├── hue_thumb.png
│   │   │   │   │   │   │   ├── picker_mask.png
│   │   │   │   │   │   │   ├── picker_thumb.png
│   │   │   │   │   │   │   └── yui.css
│   │   │   │   │   │   └── yui.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── uploadimage
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── uploadwidget
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── widget
│   │   │   │   │   ├── images
│   │   │   │   │   │   └── handle.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── tt.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── wsc
│   │   │   │   │   ├── dialogs
│   │   │   │   │   │   ├── ciframe.html
│   │   │   │   │   │   ├── tmpFrameset.html
│   │   │   │   │   │   ├── wsc_ie.js
│   │   │   │   │   │   ├── wsc.css
│   │   │   │   │   │   └── wsc.js
│   │   │   │   │   ├── icons
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   └── spellchecker.png
│   │   │   │   │   │   └── spellchecker.png
│   │   │   │   │   ├── lang
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── cy.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en-au.js
│   │   │   │   │   │   ├── en-ca.js
│   │   │   │   │   │   ├── en-gb.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── eo.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fo.js
│   │   │   │   │   │   ├── fr-ca.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── gu.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── ku.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   ├── mn.js
│   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── no.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── pt-br.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sr-latn.js
│   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── ug.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-cn.js
│   │   │   │   │   │   └── zh.js
│   │   │   │   │   ├── skins
│   │   │   │   │   │   └── moono-lisa
│   │   │   │   │   │       └── wsc.css
│   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   ├── plugin.js
│   │   │   │   │   └── README.md
│   │   │   │   ├── xml
│   │   │   │   │   └── plugin.js
│   │   │   │   ├── icons_hidpi.png
│   │   │   │   └── icons.png
│   │   │   ├── skins
│   │   │   │   ├── moono
│   │   │   │   │   ├── images
│   │   │   │   │   │   ├── hidpi
│   │   │   │   │   │   │   ├── close.png
│   │   │   │   │   │   │   ├── lock-open.png
│   │   │   │   │   │   │   ├── lock.png
│   │   │   │   │   │   │   └── refresh.png
│   │   │   │   │   │   ├── arrow.png
│   │   │   │   │   │   ├── close.png
│   │   │   │   │   │   ├── lock-open.png
│   │   │   │   │   │   ├── lock.png
│   │   │   │   │   │   ├── refresh.png
│   │   │   │   │   │   └── spinner.gif
│   │   │   │   │   ├── dialog_ie.css
│   │   │   │   │   ├── dialog_ie7.css
│   │   │   │   │   ├── dialog_ie8.css
│   │   │   │   │   ├── dialog_iequirks.css
│   │   │   │   │   ├── dialog.css
│   │   │   │   │   ├── editor_gecko.css
│   │   │   │   │   ├── editor_ie.css
│   │   │   │   │   ├── editor_ie7.css
│   │   │   │   │   ├── editor_ie8.css
│   │   │   │   │   ├── editor_iequirks.css
│   │   │   │   │   ├── editor.css
│   │   │   │   │   ├── icons_hidpi.png
│   │   │   │   │   ├── icons.png
│   │   │   │   │   └── readme.md
│   │   │   │   └── moono-lisa
│   │   │   │       ├── images
│   │   │   │       │   ├── hidpi
│   │   │   │       │   │   ├── close.png
│   │   │   │       │   │   ├── lock-open.png
│   │   │   │       │   │   ├── lock.png
│   │   │   │       │   │   └── refresh.png
│   │   │   │       │   ├── arrow.png
│   │   │   │       │   ├── close.png
│   │   │   │       │   ├── lock-open.png
│   │   │   │       │   ├── lock.png
│   │   │   │       │   ├── refresh.png
│   │   │   │       │   └── spinner.gif
│   │   │   │       ├── dialog_ie.css
│   │   │   │       ├── dialog_ie8.css
│   │   │   │       ├── dialog_iequirks.css
│   │   │   │       ├── dialog.css
│   │   │   │       ├── editor_gecko.css
│   │   │   │       ├── editor_ie.css
│   │   │   │       ├── editor_ie8.css
│   │   │   │       ├── editor_iequirks.css
│   │   │   │       ├── editor.css
│   │   │   │       ├── icons_hidpi.png
│   │   │   │       ├── icons.png
│   │   │   │       └── readme.md
│   │   │   ├── vendor
│   │   │   │   └── promise.js
│   │   │   ├── bender-runner.config.json
│   │   │   ├── build-config.js
│   │   │   ├── CHANGES.md
│   │   │   ├── ckeditor.js
│   │   │   ├── config.js
│   │   │   ├── contents.css
│   │   │   ├── LICENSE.md
│   │   │   ├── README.md
│   │   │   ├── SECURITY.md
│   │   │   └── styles.js
│   │   ├── ckeditor_uploader
│   │   │   └── admin_base.css
│   │   ├── file-icons
│   │   │   ├── doc.png
│   │   │   ├── file.png
│   │   │   ├── pdf.png
│   │   │   ├── ppt.png
│   │   │   ├── swf.png
│   │   │   ├── txt.png
│   │   │   └── xls.png
│   │   ├── galleriffic
│   │   │   ├── css
│   │   │   │   ├── basic.css
│   │   │   │   ├── black.css
│   │   │   │   ├── caption.png
│   │   │   │   ├── galleriffic-1.css
│   │   │   │   ├── galleriffic-2.css
│   │   │   │   ├── galleriffic-3.css
│   │   │   │   ├── galleriffic-4.css
│   │   │   │   ├── galleriffic-5.css
│   │   │   │   ├── jush.css
│   │   │   │   ├── loader.gif
│   │   │   │   ├── loaderWhite.gif
│   │   │   │   ├── nextPageArrow.gif
│   │   │   │   ├── nextPageArrowWhite.gif
│   │   │   │   ├── prevPageArrow.gif
│   │   │   │   ├── prevPageArrowWhite.gif
│   │   │   │   └── white.css
│   │   │   └── js
│   │   │       ├── jquery-1.3.2.js
│   │   │       ├── jquery.galleriffic.js
│   │   │       ├── jquery.history.js
│   │   │       ├── jquery.opacityrollover.js
│   │   │       └── jush.js
│   │   └── ckeditor-init.js
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── TCC_DjangoScrumKipo
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── urls.cpython-39.pyc
│   │   ├── wsgi.cpython-310.pyc
│   │   └── wsgi.cpython-39.pyc
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .DS_Store
├── backup_original_venda_livros.db
├── backup.db
├── db.sqlite3
├── dependencias.sh
├── kiposcrum_backup.db-journal
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── requirements.txt

````

## Content Mapping do Sistema Calliandra

(último update: 24/07/2022)

![Img](https://github.com/gui1080/TCC_ProjetoCalliandra/blob/master/Midia%20Externa/content_mapping.png)

## Sobre

A Calliandra (*Calliandra dysantha Benth*) é típicamente conhecida como a flor símbolo do Cerrado, de flores vermelhas e delicadas. Ela tem uso medicinal popular, é uma planta amplamente usada para paisagismo. O Cerrado é reconhecido como a savana com maior biodiversidade do mundo, apesar de muitas espécies estarem ameaçadas de extinção.


[KIPO]: "https://www.researchgate.net/publication/282939286_KIPO_the_knowledge-intensive_process_ontology"

[SCRUM]: "https://www.researchgate.net/publication/260480541_Integration_of_classical_and_agile_project_management_methodologies_based_on_ontological_models"

[readthedocs]: "https://owlready2.readthedocs.io/en/v0.37/#"
