"""
Ryan McGregor, 18Dec2021
AOC2021:Day11
https://adventofcode.com/2021/day/11
"""

from aocd import get_data

TEST_SET_1_RAW = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

class CaveSystem():
    """
    Class to manage a cave system map and determine number of paths.
    Input: List of cave connections.
    Output: None
    """
    cavemap = {'start': [] ,'end': []}

    def __init__(self, cave_connections):
        for connection in cave_connections:
            conn_pair = connection.split('-')
            for idx, node in enumerate(conn_pair):
                if node not in self.cavemap:
                    self.cavemap[node] = [conn_pair[abs(idx - 1)]]
                else:
                    self.cavemap[node].append(conn_pair[abs(idx - 1)])

    def find_paths(self, small_cave_limit=1):
        """
        Recursive function for finding all potential paths through a cave system.
        Input: small_cave_limit (int, default 1)
        Output: List of Paths (List of Nodes(str))
        """
        nodes_visited = []
        paths = []
        self.__find_path(node='start',
                         nodes_visited=nodes_visited,
                         paths=paths,
                         small_cave_limit=small_cave_limit)
        return paths

    def __find_path(self, node, nodes_visited, paths, small_cave_limit):
        nodes_visited.append(node)
        if node == 'end':
            paths.append(nodes_visited.copy())
        else:
            for connection in self.cavemap[node]:
                if connection != 'start':
                    retraces = nodes_visited.copy()
                    for unique in set(nodes_visited):
                        retraces.remove(unique)
                    if (connection.isupper() or
                        connection not in nodes_visited or
                        len([x for x in retraces if x.islower()]) < (small_cave_limit - 1)):
                        self.__find_path(node=connection,
                                    nodes_visited=nodes_visited.copy(),
                                    paths=paths,
                                    small_cave_limit=small_cave_limit)

if __name__ == '__main__':

    # ## Test Set 1 (pt1):
    # ## 10 Potential Paths (pt1), 36 Potential Paths (pt2)
    # test_system = CaveSystem(TEST_SET_1_RAW.split('\n'))
    # print('Test_System_1:')
    # print(f'Pt1: {len(test_system.find_paths())}')
    # print(f'Pt2: {len(test_system.find_paths(2))}')
    # pprint(test_system.find_paths(2))

    cave_system = CaveSystem(get_data(year=2021, day=12).split('\n'))
    print(len(cave_system.find_paths(2)))
