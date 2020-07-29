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
        self.assertEqual({'login': "The field 'login' cannot be left blank."}, response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_register_without_senha(self):
        # Given
        payload = json.dumps({
            "login": "ana",
        })

        # When
        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual({'senha': "The field 'senha' cannot be left blank."}, response.json['message'])
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

    def test_update_usuario_and_try_to_login(self):
        # Given
        login = "bob"
        senha = "1234"
        user_payload = json.dumps({
            "login": login,
            "senha": senha
        })

        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)

        # When
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        # Then
        self.assertEqual(str, type(response.json['access_token']))
        self.assertEqual(200, response.status_code)
