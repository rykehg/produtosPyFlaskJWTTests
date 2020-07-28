import json

from tests.BaseCase import BaseCase


class TestDeleteProduto(BaseCase):

    def test_delete_produto_response(self):
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
        response = self.app.delete('/produtos/echo',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("Produto deleted.", response.json['message'])
        self.assertEqual(200, response.status_code)

    def test_delete_not_existent_produto(self):
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
        response = self.app.delete('/produtos/alpha',
                                   headers={"Content-Type": "application/json",
                                            "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("Produto not found.",
                         response.json['message'])
        self.assertEqual(404, response.status_code)

    def test_delete_produto_with_logout_user(self):
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
        response = self.app.delete('/produtos/echo',
                                   headers={"Content-Type": "application/json",
                                            "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("You have been logged out.", response.json['message'])
        self.assertEqual(401, response.status_code)
