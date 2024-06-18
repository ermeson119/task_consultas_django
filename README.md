<h1>Inicializar um projeto em Django</h1>

<ol>
  <li>python -m venv .venv</li>
  <li>.venv/Script/activate</li>
  <li>pip install django</li>
  <li>django-admin startproject "NOME DO PROJETO" . </li>
  <li>django-admin startapp "NOME DO APP"</li>
  <li>python manage.py runserver</li>
</ol>

<h1>Criar super usuário</h1>
<ol>
  <li>python manage.py runserver</li>
</ol>


<h1>Criar banco de dados - Atualizar</h1>
<ol>
  <p>A primeira vez: python manage.py migrate</p>

  <p>Depois de criar o app a sequencia é essa.</p>
  <li>python manage.py makemigrations "Nome do APP"</li>
  <li>python manage.py migrate</li>
</ol>

