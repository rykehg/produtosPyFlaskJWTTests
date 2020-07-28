import json

from tests.BaseCase import BaseCase


class TestUsarioLogin(BaseCase):

    def test_successful_login(self):
        # Given
        login = "ana"
        senha = "1234"
        payload = json.dumps({
            "login": login,
            "senha": senha
        })
        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        # When
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=payload)

        # Then
        self.assertEqual(str, type(response.json['access_token']))
        self.assertEqual(200, response.status_code)

    def test_login_with_invalid_login(self):
        # Given
        login = "bob"
        senha = "asdf"
        payload = {
            "login": login,
            "senha": senha
        }
        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # When
        payload['login'] = "toby"
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # Then
        self.assertEqual("The username or password is incorrect.",
                         response.json['message'])
        self.assertEqual(401, response.status_code)

    def test_login_with_invalid_senha(self):
        # Given
        login = "eve"
        senha = "4321"
        payload = {
            "login": login,
            "senha": senha
        }
        response = self.app.post('/cadastro',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # When
        payload['senha'] = "1234"
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(payload))

        # Then
        self.assertEqual("The username or password is incorrect.",
                         response.json['message'])
        self.assertEqual(401, response.status_code)
