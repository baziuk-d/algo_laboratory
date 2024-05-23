import unittest
from src import read_csv, find_min_cable_length, Graph, UnionFind

class TestReadCSV(unittest.TestCase):
    def test_minimum_spanning_tree_algorithm(self):
        test_csv_path = "communication_wells.csv"
        graph, union_structure = read_csv(test_csv_path)
        min_cable_length = find_min_cable_length((graph, union_structure))
        self.assertEqual(min_cable_length, 150)

    def test_unconnected_minimum_spanning_tree_algorithm(self):
        test_csv_path = "disconnected_wells.csv"
        graph, union_structure = read_csv(test_csv_path)
        min_cable_length = find_min_cable_length((graph, union_structure))
        self.assertEqual(min_cable_length, -1)

    def test_read_csv(self):
        test_csv_path = "communication_wells.csv"
        graph, union_structure = read_csv(test_csv_path)
        self.assertIsInstance(graph, Graph)
        self.assertIsInstance(union_structure, UnionFind)

if __name__ == '__main__':
    unittest.main()