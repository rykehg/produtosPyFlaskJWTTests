import json

from tests.BaseCase import BaseCase


class TestDeleteUsuario(BaseCase):

    def test_delete_usuario_response(self):
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

        # When
        response = self.app.delete('/usuarios/1',
                                   headers={"Content-Type": "application/json",
                                             "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("Usuario deleted.", response.json['message'])
        self.assertEqual(200, response.status_code)

    def test_delete_not_existent_usuario(self):
        # Given
        login = "bob"
        senha = "1234"
        user_payload = json.dumps({
            "login": login,
            "senha": senha
        })

        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=user_payload)

        response = self.app.post('/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['access_token']

        # When
        response = self.app.delete('/usuarios/2',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("Usuario not found.", response.json['message'])
        self.assertEqual(404, response.status_code)


    def test_delete_usuarios_with_logout_user(self):
        # Given
        login = "bob"
        senha = "1234"
        user_payload = json.dumps({
            "login": login,
            "senha": senha
        })

        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=user_payload)

        response = self.app.post('/login', headers={"Content-Type": "application/json"}, data=user_payload)
        login_token = response.json['access_token']
        response = self.app.post('/logout',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        # When
        response = self.app.delete('/usuarios/1',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        # Then
        self.assertEqual("You have been logged out.", response.json['message'])
        self.assertEqual(401, response.status_code)
