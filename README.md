# Events Connect

Api para eventos criada para fins educacionais de aprendizado durante a NLW Connect da RocketSeat.

## setup

### banco de dados

- ter instalado o phyton
- rodar no terminal o comando `phyton3` ou `py`
- ao entrar no terminal do python rodar o comando

  ```
  import sqlite3
  sqlite3.connect('schema.db')
  ```

- com o schema feito basta se conectar a ela através de um administrador de banco de dados

### criação de um ambiente virtual

- Segue os seguintes links para instalar:
  o pacote virtual env:
  https://pypi.org/project/virtualenv/

  e o guia de usuário
  https://virtualenv.pypa.io/en/latest/user_guide.html

## tecnologias do projeto

- **Cerberus**:
  Uma biblioteca de validação de dados para Python, que permite definir regras para garantir que os dados recebidos estejam corretos e no formato esperado.

- **Flask**:
  Um microframework web para Python que facilita a criação de aplicações web simples e escaláveis, oferecendo flexibilidade e extensibilidade.

- **pytest**:
  Uma framework para testes automatizados em Python, que facilita a escrita e execução de testes unitários e de integração, com recursos avançados como fixtures e asserts.

- **SQLAlchemy**:
  Uma biblioteca ORM (Object-Relational Mapping) para Python, que facilita a interação com bancos de dados relacionais, permitindo mapear tabelas para classes Python e realizando operações SQL de forma eficiente e intuitiva.

## rotas da api

--
**events**
--

- "/events" -> Método POST
  Criação de um evento. Exemplo de body:

```
{
  "data": {
    "name": "evento rocket summer"
  }
}
```

--
**events_links**
--

- "/events_links" -> Método POST
  Criação de um link para evento. Exemplo de body:

```
{
  "data": {
    "event_id": 3,
    "subscriber_id": 2
  }
}
```

--
**subscriber**
--

- "/subscriber" -> Método POST
  Inscrição de alguém em um evento. Exemplo de body:

```
{
  "data": {
    "name": "inscrito 780",
    "email": "inscrito780@gmail.com",
    "evento_id": 5
  }
}
```

- "/subscriber/link/:link/event/:event_id" -> Método GET
  Buscar inscritos pelo link e id do evento. Exemplo de resposta:

```
{
  "data": {
      "attributes": [
          {
              "email": "inscrito780@gmail.com",
              "nome": "inscrito 780"
          }
      ],
      "count": 1,
      "type": "Subscribers"
  }
}
```

- "/subscriber/ranking/event/:event_id" -> Método GET
  Obter um ranking de inscrições por link para um determinado evento. Exemplo de resposta:

```
{
  "data": {
      "attributes": [
          {
              "link": "olaMundo2",
              "total_subscribers": 1
          },
          {
              "link": "olaMUndo",
              "total_subscribers": 1
          }
      ],
      "count": 2,
      "type": "Ranking"
  }
}
```
