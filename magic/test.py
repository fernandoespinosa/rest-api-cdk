import unittest
from echo import Echo

class TestEcho(unittest.TestCase):
    def setUp(self):
        self.echo = Echo()

    def test_repeat(self):
        self.assertEqual(self.echo.repeat("hello"), "hello")
        self.assertEqual(self.echo.repeat("world"), "world")
        self.assertEqual(self.echo.repeat(""), "")

    def test_loudly(self):
        self.assertEqual(self.echo.loudly("hello"), "HELLO")
        self.assertEqual(self.echo.loudly("world"), "WORLD")
        self.assertEqual(self.echo.loudly(""), "")

if __name__ == '__main__':
    unittest.main()
