import unittest
from root_vertex import find_root_vertex
class TestFindRootVertex(unittest.TestCase):
    def test1(self):
        graph = [[]]
        self.assertEqual(find_root_vertex(graph), 0)

    def test2(self):
        graph = [[1], []]
        self.assertEqual(find_root_vertex(graph), 0)

    def test3_multigraph_(self):
        graph = [[1, 2, 3], [2], [2], [4], []]
        self.assertEqual(find_root_vertex(graph), 0)


if __name__ == '__main__':
    unittest.main()