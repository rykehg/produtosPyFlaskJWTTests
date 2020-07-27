import unittest

from app import app
from models.sql_alchemy import db, initialize_db


class BaseCase(unittest.TestCase):

    def setUp(self):
        super(BaseCase, self).setUp()
        app.testing = True
        initialize_db(app)
        self.app = app
        self.app = app.test_client()
        self.app.application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
        self.db = db
        self.db.app = self.app

        self.client = self.app.application.test_client()
        self.app_context = self.app.application.app_context()
        self.app_context.push()

    def tearDown(self):
        # Delete Database collections after the test is complete
        # self.db.session.rollback()
        self.db.drop_all()
        super(BaseCase, self).tearDown()
