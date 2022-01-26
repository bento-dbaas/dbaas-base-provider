from dbaas_base_provider.log import log_this
from unittest import TestCase
import mock


class TestLog(TestCase):
    def test_logx(self):
        m = mock.MagicMock()
        m.values = "MyData"
        with mock.patch("dbaas_base_provider.log.request", m):
            @log_this
            def f_teste(x, y):
                try:
                    return x / y
                except Exception as e:
                    return "Error"

            self.assertEqual(f_teste(10, 5), 10 / 5, "Function executed without error")
            self.assertEqual(f_teste(10, 0), "Error", "Function executed with error")
