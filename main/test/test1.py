import unittest
from src import array_monotonic

class Test(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(array_monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(array_monotonic([5, 4, 3, 2, 1]))

    def test_not_monotonic(self):
        self.assertFalse(array_monotonic([1, 2, 2, 3, 2, 4]))

    def test_not_monotonic2(self):
        self.assertEqual(array_monotonic([2, 2, 2, 2, 2, 3]), True)

    def test_not_monotonic3(self):
        self.assertEqual(array_monotonic([2, 2, 2, 2, 2, 1]), True)

    def test_not_monotonic4(self):
        self.assertEqual(array_monotonic([1, 1, 1, 1, 1, 0]), True)

if __name__ == '__main__':
    unittest.main()