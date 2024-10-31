import unittest
from app import add_numbers 
class TestApp(unittest.TestCase):
    def test_negative_sum(self):
        result = add_numbers(-5, -10)
        self.assertEqual(result, -15, "Should be -15")
