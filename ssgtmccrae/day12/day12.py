
"""
Ryan McGregor, 18Dec2021
AOC2021:Day11
https://adventofcode.com/2021/day/11
"""

from pprint import pprint
from aocd import get_data
import numpy as np

TEST_SET_1_RAW = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST_SET_2_RAW = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

class CaveSystem():
    """
    Class to manage a cave system map and determine number of paths.
    Input: List of cave connections.
    Output: None
    """
    cavemap = {'start': [] ,'end': []}
    __paths = []

    def __init__(self, cave_connections):
        for connection in cave_connections:
            conn_pair = connection.split('-')
            for idx, node in enumerate(conn_pair):
                if node not in self.cavemap:
                    self.cavemap[node] = [conn_pair[abs(idx - 1)]]
                else:
                    self.cavemap[node].append(conn_pair[abs(idx - 1)])

    @property
    def paths(self):
        """
        Recursive function for finding all potential paths through a cave system.
        Input: None
        Output: List of Paths (List of Nodes(str))
        """
        if len(self.__paths) == 0:
            nodes_visited = []
            self.__find_path('start', nodes_visited)
        return(self.__paths)

    def __find_path(self, node, nodes_visited):
        nodes_visited.append(node)
        print(f'nodes_visited: {nodes_visited}')
        print(f'node: {node}')
        for connection in self.cavemap[node]:
            if connection == 'end':
                nodes_visited.append(connection)
                self.__paths.append(nodes_visited.copy())
            if connection not in nodes_visited or connection.isupper():
                self.__find_path(connection, nodes_visited.copy())






if __name__ == '__main__':

    # ## Test Set 1: 10 Potential Paths
    # test_system = CaveSystem(TEST_SET_1_RAW.split('\n'))
    # pprint(test_system.paths)

    # ## Test Set 2: 226 Potential Paths
    # test_system = CaveSystem(TEST_SET_2_RAW.split('\n'))
    # print(len(test_system.paths))

    cave_system = CaveSystem(get_data(year=2021, day=12).split('\n'))
    print(len(cave_system.paths))
