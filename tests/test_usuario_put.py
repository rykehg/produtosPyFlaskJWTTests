import json

from tests.BaseCase import BaseCase


class TestPutUsuario(BaseCase):

    def test_update_usuario_login_response(self):
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
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        user_update_payload = {
            "login": "toby",
            "senha": "1234"
        }

        response = self.app.put('/usuarios/1',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(user_update_payload))

        # When
        usuario_data = response.json

        # Then
        self.assertEqual(1, usuario_data['usuario_id'])
        self.assertEqual("toby", usuario_data['login'])
        self.assertEqual(200, response.status_code)

    def test_update_usuario_senha_response(self):
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
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        user_update_payload = {
            "login": "bob",
            "senha": "asdf"
        }

        response = self.app.put('/usuarios/1',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(user_update_payload))

        # When
        usuario_data = response.json

        # Then
        self.assertEqual(1, usuario_data['usuario_id'])
        self.assertEqual("bob", usuario_data['login'])
        self.assertEqual(200, response.status_code)

    def test_update_usuario_with_no_senha(self):
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
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        user_update_payload = {
            "login": "bob"
        }

        # When
        response = self.app.put('/usuarios/1',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(user_update_payload))

        # Then
        self.assertEqual({'senha': "The field 'senha' cannot be left blank."},
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_update_usuario_with_no_login(self):
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
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        user_update_payload = {
            "senha": "1234"
        }

        # When
        response = self.app.put('/usuarios/1',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(user_update_payload))

        # Then
        self.assertEqual({'login': "The field 'login' cannot be left blank."},
                         response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_update_not_existent_usuario(self):
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
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        user_update_payload = {
            "login": "toby",
            "senha": "1234"
        }

        # When
        response = self.app.put('/usuarios/2',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(user_update_payload))

        # Then
        self.assertEqual("Usuario not found.", response.json['message'])
        self.assertEqual(404, response.status_code)

    def test_update_usuarios_with_logout_user(self):
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
        response = self.app.post('/login',
                                 headers={"Content-Type": "application/json"},
                                 data=user_payload)
        login_token = response.json['access_token']

        user_update_payload = {
            "login": "toby",
            "senha": "1234"
        }
        response = self.app.post('/logout',
                                 headers={"Content-Type": "application/json",
                                          "Authorization": f"Bearer {login_token}"})
        # When
        response = self.app.put('/usuarios/2',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(user_update_payload))
        # Then
        self.assertEqual("You have been logged out.", response.json['message'])
        self.assertEqual(401, response.status_code)
