import json

from tests.BaseCase import BaseCase


class TestGetProduto(BaseCase):

    def test_get_produto_response(self):
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

        response = self.app.get('/produtos/echo',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"})

        # When
        produto_data = response.json

        # Then
        self.assertEqual(nome, produto_data['nome'])
        self.assertEqual(quantidade, produto_data['quantidade'])
        self.assertEqual(valor, produto_data['valor'])
        self.assertEqual(descricao, produto_data['descricao'])
        self.assertEqual(200, response.status_code)

    def test_get_not_existent_produto(self):
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
        response = self.app.get('/produtos/alpha',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("Produto not found.",
                         response.json['message'])
        self.assertEqual(404, response.status_code)

    def test_get_produto_with_logout_user(self):
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

        response = self.app.post('/logout',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"})
        # When
        response = self.app.get('/produtos/echo',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("You have been logged out.", response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_get_all_produto_response(self):
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

        nome1 = "Echo Produto"
        quantidade1 = 33
        valor1 = 99.89
        descricao1 = "Echo produto descrição importante aqui."
        produto_payload = {
            "nome": nome1,
            "quantidade": quantidade1,
            "valor": valor1,
            "descricao": descricao1
        }
        response = self.app.post('/produtos/echo',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload))

        nome2 = "Alpha Produto"
        quantidade2 = 10
        valor2 = 34.56
        descricao2 = "Alpha produto descrição importante aqui."
        produto_payload2 = {
            "nome": nome2,
            "quantidade": quantidade2,
            "valor": valor2,
            "descricao": descricao2
        }
        response = self.app.post('/produtos/alpha',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(produto_payload2))

        response = self.app.get('/produtos',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"})

        # When
        produto_data = response.json

        # Then
        self.assertEqual(nome1, produto_data['Produtos'][0]['nome'])
        self.assertEqual(quantidade1, produto_data['Produtos'][0]['quantidade'])
        self.assertEqual(valor1, produto_data['Produtos'][0]['valor'])
        self.assertEqual(descricao1, produto_data['Produtos'][0]['descricao'])
        self.assertEqual(nome2, produto_data['Produtos'][1]['nome'])
        self.assertEqual(quantidade2, produto_data['Produtos'][1]['quantidade'])
        self.assertEqual(valor2, produto_data['Produtos'][1]['valor'])
        self.assertEqual(descricao2, produto_data['Produtos'][1]['descricao'])
        self.assertEqual(200, response.status_code)

    def test_get_all_produto_with_logout_user(self):
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

        response = self.app.post('/logout',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"})
        # When
        response = self.app.get('/produtos',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("You have been logged out.", response.json['message'])
        self.assertEqual(401, response.status_code)
