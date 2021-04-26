from unittest import TestCase

from dbaas_base_provider.baseCredential import BaseCredential
from dbaas_base_provider.base import BaseProviderObject
from unittest.mock import patch, MagicMock, PropertyMock

from fakes import MONGO_ENDPOINT, MONGODB_DB, MONGODB_HOST, MONGODB_PORT,\
                  MONGODB_USER, MONGODB_PWD, FAKE_CREDENTIAL


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
        cred = BaseCredential(PROVIDER, ENVIRONMENT)

        self.assertIsInstance(cred, BaseCredential)


    @patch('dbaas_base_provider.baseCredential.MongoClient')
    def test_credential_hp_connect_with_mongo_by_endpoint(self, mc):
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred.provider_type = "host_provider"
        cred.MONGO_ENDPOINT = self.MONGO_ENDPOINT
        cred.MONGODB_DB = self.MONGODB_DB
        mc.return_value = {self.MONGODB_DB: ""}
        cred.db

        self.assertTrue(mc.called)

    @patch('dbaas_base_provider.baseCredential.MongoClient')
    def test_credential_hp_connect_with_mongo_by_mongo_credentials(self, mc):
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred.provider_type = "host_provider"
        cred.MONGODB_HOST = self.MONGODB_HOST
        cred.MONGODB_DB = self.MONGODB_DB
        cred.MONGODB_PORT = self.MONGODB_PORT
        cred.MONGODB_PWD = self.MONGODB_PWD
        cred.MONGODB_USER = self.MONGODB_USER
        mc.return_value = {self.MONGODB_DB: ""}
        cred.db

        self.assertTrue(mc.called)

    @patch('dbaas_base_provider.baseCredential.MongoClient')
    def test_credential_vp_connect_with_mongo(self, mc):
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred.provider_type = "volume_provider"
        cred.MONGODB_PARAMS = {}
        cred.MONGODB_DB = self.MONGODB_DB
        mc.return_value = {self.MONGODB_DB: ""}
        cred.db

        self.assertTrue(mc.called)

    @patch('dbaas_base_provider.baseCredential.MongoClient')
    def test_credential_prop(self, mc):
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred.provider_type = "volume_provider"
        cred.MONGODB_PARAMS = {}
        cred.MONGODB_DB = self.MONGODB_DB
        mc.return_value = {self.MONGODB_DB: {"credentials": FAKE_CREDENTIAL}}

        self.assertEqual(cred.credential, FAKE_CREDENTIAL)
        self.assertTrue(mc.called)

    @patch('dbaas_base_provider.baseCredential.MongoClient')
    def test_content_prop_with_no_content(self, mc):
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred.MONGODB_PARAMS = {}
        cred.MONGODB_DB = self.MONGODB_DB
        mc.return_value = {self.MONGODB_DB: {"credentials": FAKE_CREDENTIAL}}

        self.assertRaises(NotImplementedError, lambda: cred.content)

    @patch('dbaas_base_provider.baseCredential.MongoClient')
    def test_content_prop(self, mc):
        fake_content = "fake_cont"
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred = BaseCredential(PROVIDER, ENVIRONMENT)
        cred.MONGODB_PARAMS = {}
        cred.MONGODB_DB = self.MONGODB_DB
        mc.return_value = {self.MONGODB_DB: {"credentials": FAKE_CREDENTIAL}}
        cred._content = fake_content
        self.assertEqual(cred.content, fake_content)
