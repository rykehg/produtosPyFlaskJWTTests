import json
from tests.BaseCase import BaseCase


class TestCreateUsuario(BaseCase):

    def test_successful_create_usuario(self):
        # Given
        payload = json.dumps({
            "login": "bob",
            "senha": "asdf"
        })

        # When
        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['message']))
        self.assertEqual(201, response.status_code)

    def test_register_without_login(self):
        # Given
        payload = json.dumps({
            "senha": "1234"
        })

        # When
        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("The field 'login' cannot be left blank.", response.json['login'])
        self.assertEqual(400, response.status_code)
'''
    def test_register_without_senha(self):
        # Given
        payload = json.dumps({
            "login": "ana",
        })

        # When
        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("The field 'senha' cannot be left blank.", response.json['senha'])
        self.assertEqual(400, response.status_code)

    def test_creating_already_existing_user(self):
        # Given
        payload = json.dumps({
            "login": "paulo",
            "senha": "1234"
        })
        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("The login 'paulo' already exists.", response.json['message'])
        self.assertEqual(200, response.status_code)
'''
