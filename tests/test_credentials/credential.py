from unittest import TestCase

from base_provider import BaseCredential
from base_provider.base import BaseProviderObject
from unittest.mock import patch, MagicMock, PropertyMock

from fakes import MONGO_ENDPOINT, MONGODB_DB


PROVIDER = "fake"
ENVIRONMENT = "dev"

class TestCredential(TestCase):

    def setUp(self):
        self.MONGO_ENDPOINT = MONGO_ENDPOINT
        self.MONGODB_DB = MONGODB_DB

    def test_credential_instance(self):
        cred = BaseCredential('host_provider', PROVIDER, ENVIRONMENT)

        self.assertIsInstance(cred, BaseCredential)

    def test_credential_invalid_provider_db(self):
        cred = BaseCredential('invalid_provider', PROVIDER, ENVIRONMENT)
        self.assertRaises(NotImplementedError, lambda: cred.db)

    @patch('.base_provider.base.MongoClient')
    def test_credential_hp_connect_with_mongo_by_endpoint(self, mc):
        cred = BaseCredential('host_provider', PROVIDER, ENVIRONMENT)
        mc.return_value = "MONGODB_DB"
        db = cred.db

        self.assertFalse(mc.called)
        print(db)