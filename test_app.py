import unittest

from app import add, multiply, greet


class TestApp(unittest.TestCase):
    def test_init(self):
        self.assertTrue(True)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_greet(self):
        self.assertEqual(greet("CodeBuild"), "Hello, CodeBuild!")


if __name__ == "__main__":
    unittest.main()