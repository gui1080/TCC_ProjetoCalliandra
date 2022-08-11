# Script shell para instalação de dependências

echo "Hello $USER"
echo "Se certifique que seu Python3 está em dia (Python 3.9.7)"
python3 --version
echo "Instalando ambiente virtual"
pip3 install virtualenv
python3 -m venv venv
echo "Para rodar se deve rodar -> 'source venv/bin/activate'"
source venv/bin/activate
pip3 install Owlready2
pip3 install Django
pip install django-crispy-form
pip3 install django-crispy-form
pip3 install --upgrade pip
pip3 install numpy
echo "Rodando Django -> 'python3 manage.py runserver'"
python3 manage.py runserver
echo "Tchau $USER"
