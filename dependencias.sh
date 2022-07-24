# Script shell para instalação de dependências

echo "Hello $USER"
echo "Se certifique que seu Python3 está em dia"
python3 --version
echo "Instalando ambiente virtual"
pip3 install virtualenv
python3 -m venv venv
echo "Para rodar se deve rodar -> 'source venv/bin/activate'"
source venv/bin/activate
pip3 install Owlready2
pip3 install Django
pip install numpy
echo "Rodando Django -> 'python3 manage.py runserver'"
python3 manage.py runserver
echo "Tchau $USER"
