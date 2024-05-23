import unittest
from src import morris_pratt_search, build_prefix_function

class TestKMP(unittest.TestCase):
    def test_build_prefix_table(self):
        pattern = "ABCABD"
        expected_prefix_table = [0, 0, 0, 1, 2, 0]
        self.assertEqual(build_prefix_function(pattern), expected_prefix_table)

    def test_kmp_search(self):
        text = "ABCABEABCABCABD"
        pattern = "ABCABD"
        self.assertEqual(morris_pratt_search(text, pattern), [9])

    def test_kmp_search_single_match(self):
        text = "Персональні Дані!"
        pattern = "Дані"
        self.assertEqual(morris_pratt_search(text, pattern), [12])

if __name__ == '__main__':
    unittest.main()