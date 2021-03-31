from unittest import TestCase

from dbaas_base_provider.version import Version


class TestProvider(TestCase):

    def setUp(self):
        pass

    def test_get_version(self):
        vrs = '0.0.11'
        v = Version(vrs).number

        self.assertEqual(v, vrs)

    def test_update_version_raise(self):
        v = Version('123')

        with self.assertRaises(TypeError):
            v.number = '456'
