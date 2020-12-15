import unittest
from rpc_microservice_challenge.lib.square_odd_numbers import square_odd_numbers


class TestSquareOddNumbers(unittest.TestCase):

    def test_squares_odd_numbers(self):
        self.assertEqual(square_odd_numbers(1, 2, 3), [1, 9])

    def test_when_no_odd_numbers_returns_empty_list(self):
        self.assertEqual(square_odd_numbers(2, 4, 6), [])

    def test_when_no_args_returns_empty_list(self):
        self.assertEqual(square_odd_numbers(), [])
