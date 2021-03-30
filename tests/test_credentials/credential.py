from unittest import TestCase

from base_provider import BaseCredential
from base_provider.base import BaseProviderObject
from unittest.mock import patch, MagicMock, PropertyMock

from fakes import MONGO_ENDPOINT, MONGODB_DB, MONGODB_HOST, MONGODB_PORT,\
                  MONGODB_USER, MONGODB_PWD


PROVIDER = "fake"
ENVIRONMENT = "dev"

class TestCredential(TestCase):

    def setUp(self):
        self.MONGO_ENDPOINT = MONGO_ENDPOINT
        self.MONGODB_DB = MONGODB_DB
        self.MONGODB_HOST = MONGODB_HOST
        self.MONGODB_USER = MONGODB_USER
        self.MONGODB_PWD = MONGODB_PWD
        self.MONGODB_PORT = MONGODB_PORT

    def test_credential_instance(self):
        cred = BaseCredential('host_provider', PROVIDER, ENVIRONMENT)

        self.assertIsInstance(cred, BaseCredential)

    def test_credential_invalid_provider_db(self):
        cred = BaseCredential('invalid_provider', PROVIDER, ENVIRONMENT)
        self.assertRaises(NotImplementedError, lambda: cred.db)


    @patch('base_provider.baseCredential.MongoClient')
    def test_credential_hp_connect_with_mongo_by_endpoint(self, mc):
        cred = BaseCredential('host_provider', PROVIDER, ENVIRONMENT)
        cred.MONGO_ENDPOINT = self.MONGO_ENDPOINT
        cred.MONGODB_DB = self.MONGODB_DB
        mc.return_value = {self.MONGODB_DB: ""}
        db = cred.db

        self.assertTrue(mc.called)

    @patch('base_provider.baseCredential.MongoClient')
    def test_credential_hp_connect_with_mongo_by_mongo_credentials(self, mc):
        cred = BaseCredential('host_provider', PROVIDER, ENVIRONMENT)
        cred.MONGODB_HOST = self.MONGODB_HOST
        cred.MONGODB_DB = self.MONGODB_DB
        cred.MONGODB_PORT = self.MONGODB_PORT
        cred.MONGODB_PWD = self.MONGODB_PWD
        cred.MONGODB_USER = self.MONGODB_USER
        mc.return_value = {self.MONGODB_DB: ""}
        db = cred.db

        self.assertTrue(mc.called)