from unittest import TestCase
from copy import copy, deepcopy

from dbaas_base_provider.baseProvider import BaseProvider
from dbaas_base_provider.base import BaseProviderObject
from unittest.mock import patch, MagicMock, PropertyMock

from fakes import (CredentialAddFake,
                   FAKE_PROVIDER, FAKE_SAVE_ID)

ENGINE = "fake_engine"
ENVIRONMENT = "dev"


class TestProvider(TestCase):

    def setUp(self):
        self.credential_add_cls = copy(CredentialAddFake)

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
    
    def test_provider_prop_raise(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)

        with self.assertRaises(NotImplementedError):
            prov.provider

    def test_credential_prop(self):
        credential = "fake_credential"
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        prov._credential = credential

        self.assertEqual(prov.credential, credential)

    def test_credential_prop_build_client(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        prov.build_credential = lambda: 'credential'

        self.assertEqual(prov.credential, 'credential')

    def test_credential_add_raise(self):
        prov = BaseProvider(ENVIRONMENT, ENGINE)

        with self.assertRaises(NotImplementedError):
            prov.credential_add(None)

    @patch('dbaas_base_provider.baseProvider.BaseProvider.get_credential_add')
    @patch('dbaas_base_provider.baseProvider.BaseProvider.get_provider',
           new=MagicMock(return_value=FAKE_PROVIDER))
    def test_credentaial_add_valid(self, fake_cred):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        
        fake_cred.return_value = self.credential_add_cls
        fake_cred.return_value.is_valid = lambda s, a: (True, "")
        fake_cred.return_value.save = lambda s: {'_id': FAKE_SAVE_ID}

        f = prov.credential_add(content={})

        self.assertTrue(f[0])
        self.assertEqual(f[1], FAKE_SAVE_ID)

    @patch('dbaas_base_provider.baseProvider.BaseProvider.get_credential_add')
    @patch('dbaas_base_provider.baseProvider.BaseProvider.get_provider',
           new=MagicMock(return_value=FAKE_PROVIDER))
    def test_credentaial_add_invalid(self, fake_cred):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        errmsg = "Invalid Credential"
        fake_cred.return_value = self.credential_add_cls
        fake_cred.return_value.is_valid = lambda s, a: (False, errmsg)

        f = prov.credential_add(content={})

        self.assertFalse(f[0])
        self.assertEqual(f[1], errmsg)

    @patch('dbaas_base_provider.baseProvider.BaseProvider.get_credential_add')
    @patch('dbaas_base_provider.baseProvider.BaseProvider.get_provider',
           new=MagicMock(return_value=FAKE_PROVIDER))
    def test_credentaial_add_raises_on_save(self, fake_cred):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        errmsg = "Error on save"

        def raise_(ex):
            raise ex

        fake_cred.return_value = self.credential_add_cls
        fake_cred.return_value.is_valid = lambda s, a: (True, "")
        fake_cred.return_value.save = lambda s: raise_(Exception(errmsg))

        f = prov.credential_add(content={})

        self.assertFalse(f[0])
        self.assertEqual(f[1], errmsg)

@patch('dbaas_base_provider.baseProvider.BaseProvider.get_credential_add')
@patch('dbaas_base_provider.baseProvider.BaseProvider.get_provider',
        new=MagicMock(return_value=FAKE_PROVIDER))
class TestWaits(TestCase):

    def test_call_wait_operation_without_operation(self, fake_cred):
        prov = BaseProvider(ENVIRONMENT, ENGINE)
        with self.assertRaises(EnvironmentError):
            prov.wait_operation()
