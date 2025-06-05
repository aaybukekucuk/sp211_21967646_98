import unittest
from sp211_21967646_98.shortestpath import shortest_path

class TestShortestPath(unittest.TestCase):
    def test_basic_path(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        start = 'A'
        end = 'D'
        expected_path = (4, ['A', 'B', 'C', 'D'])  # shortest_path fonksiyonu (distance, path) döndürüyor
        result = shortest_path(graph, start, end)
        self.assertEqual(result, expected_path)

if __name__ == '__main__':
    unittest.main()