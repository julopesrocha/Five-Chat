# Five Chat 
Neste exercício vamos criar um sistema de chat, onde cada usuário poderá entrar em salas de bate papo e interagir com os membros por mensagens de texto. Como se fosse o famoso Bate Papo UOL.

Para isso, cada usuário que acessar a plataforma precisa ser identificado para que suas mensagens contenham seu nome de usuário.

Vamos trabalhar com salas pré-definidas e cada uma delas terá seu histórico salvo em um banco de dados.



## Índice
* [Informações sobre o hardware](#informações-sobre-o-hardware)
* [Autenticação](#autenticação)
* [Como rodas o programa](#como-rodar-o-programa)

## Informações sobre o hardware
- Distro: Ubuntu 20.04.4 LTS
- Nome do Modelo: Intel(R) Core(TM) i3-8145U CPU @ 2.10GHz
- Arquitetura: x86_64

## Autenticação
:exclamation: A autenticação do usuário é feita através da API Gmail do Google. 
Para realizar a autenticação com Google, utilizamos o pacote Django Allauth, que permite realizar o que quisermos em termos de autenticação da aplicação.
No painel Google cloud console foram geradas as credenciais da aplicação, o ID do cliente e sua secret_key que foram setadas dentro do painel de admin do Django Rest Framework

Acesso ao endpoint de login : 
```
http://127.0.0.1:8000/accounts/login'
```
Uma vez que o login for realizado, o redirecionamento pela documentação leva diretamente à 'accounts/profile'
endpoint programado da própria API, ainda nao consegui direcionar diretamente para '/room/' onde encontramos a listagem de todas as salas contidas na aplicação

## Como rodar o programa
:thinking: Compila e executa o programa através dos comandos:
1. Vamos criar um ambiente virtual para isolar nosso pacote de dependências 
```
$ python3 -m venv env 
$ source env/bin/activate
```
2. 
```
$ pip install requirements.txt
```
3. Servir a aplicação
```
$ python manage.py runserver
```
4. Rodar os testes
```
python manage.py test
```