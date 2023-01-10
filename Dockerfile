FROM python:3.9

ENV  PYTHONUNBUFFERED=1

RUN mkdir /Calliandra

WORKDIR /Calliandra

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8081"]
