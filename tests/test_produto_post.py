import json

from tests.BaseCase import BaseCase


class TestPostProduto(BaseCase):

    def test_create_produto_response(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = "Echo Produto"
        quantidade = 33
        valor = 99.89
        descricao = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }

        # When
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))
        produto_data = response.json

        # Then
        self.assertEqual(nome, produto_data['nome'])
        self.assertEqual(quantidade, produto_data['quantidade'])
        self.assertEqual(valor, produto_data['valor'])
        self.assertEqual(descricao, produto_data['descricao'])
        self.assertEqual(201, response.status_code)

    def test_create_existing_produto(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = "Echo Produto"
        quantidade = 33
        valor = 99.89
        descricao = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # When
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # Then
        self.assertEqual("Produto id 'echo' already exists.",
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_create_produto_with_no_nome(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = None
        quantidade = 33
        valor = 99.89
        descricao = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # Then
        self.assertEqual("Request is missing required fields.",
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_create_produto_with_no_quantidade(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = "Echo Produto"
        quantidade = None
        valor = 99.89
        descricao = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # When
        produto_data = response.json

        # Then
        self.assertEqual(nome, produto_data['nome'])
        self.assertEqual(quantidade, produto_data['quantidade'])
        self.assertEqual(valor, produto_data['valor'])
        self.assertEqual(descricao, produto_data['descricao'])
        self.assertEqual(201, response.status_code)

    def test_create_produto_with_no_valor(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = "Echo Produto"
        quantidade = 33
        valor = None
        descricao = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }
        # When
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # Then
        self.assertEqual("Request is missing required fields.",
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_create_produto_with_no_descricao(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = "Echo Produto"
        quantidade = 33
        valor = 99.89
        descricao = None
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # When
        produto_data = response.json

        # Then
        self.assertEqual(nome, produto_data['nome'])
        self.assertEqual(quantidade, produto_data['quantidade'])
        self.assertEqual(valor, produto_data['valor'])
        self.assertEqual(descricao, produto_data['descricao'])
        self.assertEqual(201, response.status_code)

    def test_create_produto_with_logout_user(self):
        # Given
        user_payload = json.dumps({
            "login": "bob",
            "senha": "1234"
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        nome = "Echo Produto"
        quantidade = 33
        valor = 99.89
        descricao = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome,
            "quantidade": quantidade,
            "valor": valor,
            "descricao": descricao
        }
        response = self.app.post('/logout',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"})

        # When
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        # Then
        self.assertEqual("You have been logged out.", response.json['message'])
        self.assertEqual(401, response.status_code)
