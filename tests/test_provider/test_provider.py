from unittest import TestCase

from dbaas_base_provider import BaseProvider
from dbaas_base_provider.base import BaseProviderObject
from unittest.mock import patch, MagicMock, PropertyMock

ENGINE = "fake_engine"
ENVIRONMENT = "dev"


class TestProvider(TestCase):

    def setUp(self):
        pass

    def test_provider_initialization(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)

        self.assertEqual(prov.engine, ENGINE)

    def test_client_prop_raise(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)

        with self.assertRaises(NotImplementedError):
            prov.client

    def test_client_prop(self):
        client = "fake_client"
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        prov._client = client

        self.assertEqual(prov.client, client)

    def test_client_prop_build_client(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        prov.build_client = lambda: 'client'

        self.assertEqual(prov.client, 'client')

    def test_credential_prop_raise(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)

        with self.assertRaises(NotImplementedError):
            prov.credential

    def test_credential_prop(self):
        credential = "fake_credential"
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        prov._credential = credential

        self.assertEqual(prov.credential, credential)

    def test_credential_prop_build_client(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        prov.build_credential = lambda: 'credential'

        self.assertEqual(prov.credential, 'credential')
