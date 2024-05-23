import csv

class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def make_set(self, node):
        self.parents[node] = node
        self.ranks[node] = 0

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.ranks[root1] < self.ranks[root2]:
                self.parents[root1] = root2
            elif self.ranks[root1] > self.ranks[root2]:
                self.parents[root2] = root1
            else:
                self.parents[root2] = root1
                self.ranks[root1] += 1


class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def kruskal_mst(self, union_structure):
        edges = sorted(self.edges, key=lambda value: value[2])
        mst = []
        for start, end, weight in edges:
            if union_structure.find(start) != union_structure.find(end):
                mst.append((start, end, weight))
                union_structure.union(start, end)
        return mst

    def all_nodes_connected(self, union_structure):
        roots = set(union_structure.find(node) for node in union_structure.parents.keys())
        return len(roots) == 1


def find_min_cable_length(filename):
    graph, union_structure = filename
    mst = graph.kruskal_mst(union_structure)
    total_length = sum(weight for _, _, weight in mst)
    return total_length if graph.all_nodes_connected(union_structure) else -1

def read_csv(filepath):
    graph = Graph()
    union_structure = UnionFind()
    with open(filepath, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            if len(row) == 3:
                start, end, weight = row
                graph.add_edge(start, end, int(weight))
                union_structure.make_set(start)
                union_structure.make_set(end)
    return graph, union_structure