# Conceitos de API

Projeto desenvolvido durante o [curso](https://www.udemy.com/course/apis-restful-com-django-rest-framework) do Instrutor [Gregory Pacheco](https://www.linkedin.com/in/pachecogregory/).

## Objetivo:
- Entender o que é uma Web API RESTFul.
- Preparar o ambiente Python e Djando para desenvolvimento de Web API's.
- Entender o funcionamento Django Rest Framework.
- Criação do Projeto Django.
- Modelagem de API's.
- Serialização dos dados.
- Retornando dados estruturados.
- Executar chamadas a API utilizando verbos HTTP.
- Leitura dos dados da API utilizando JSON.
- Sistema de autorização e autenticação do Django Rest Framework.

<img src="pontos_turisticos/static/img/Mapa%20Conceitual.PNG" alt="My cool logo"/>

## O que a API pode fazer:
- Propor um novo ponto turístico
- Moderação dos pontos turísticos cadastrados
- Listagem básica dos pontos turísticos ( Lista resumida )
- Listagem completa dos pontos turísticos
- Detalhe de um ponto turístico
- Atualização de um ponto turístico por usuários autorizados
- Deleção de um ponto turístico por usuários autorizados

### Para Desenvolver:
#### Ambientes Linux:
```
python3 -m venv .venv
source .venv/bin/activate
cp env-sample .env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
#### Ambientes Windows:
```
py -3 -m venv .venv
.venv\Scripts\activate
copy env-sample .env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```