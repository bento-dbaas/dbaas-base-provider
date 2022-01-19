from dbaas_base_provider.log import log_this
from unittest import TestCase


class TestLog(TestCase):
    def test_logx(self):
        @log_this
        def f_teste(x, y):
            try:
                return x / y
            except Exception as e:
                return "Erro"

        self.assertEqual(f_teste(10, 5), 10 / 5, "Funçao executada sem erro")
        self.assertEqual(f_teste(10, 0), "Erro", "Funçao executada com erro")
