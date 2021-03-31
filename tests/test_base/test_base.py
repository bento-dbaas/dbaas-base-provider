from unittest import TestCase
from dbaas_base_provider.base import BaseProviderObject

class TestBase(TestCase):
    
    def test_instance_base(self):
        ins = BaseProviderObject()

        self.assertIsInstance(ins, BaseProviderObject)
