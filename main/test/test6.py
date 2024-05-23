import unittest
from career import calculate_max_experience


class TestMainFunction(unittest.TestCase):
    def test_calculate_max_experience1(self):
        levels = [
            [4],
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(calculate_max_experience(levels), 16)

    def test_calculate_max_experience2(self):
        levels = [
            [3],
            [2, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
        self.assertEqual(calculate_max_experience(levels), 22)

    def test_calculate_max_experience3(self):
        levels = [
            [2],
            [3],
            [4, 5]
        ]
        self.assertEqual(calculate_max_experience(levels), 10)

if __name__ == '__main__':
    unittest.main()