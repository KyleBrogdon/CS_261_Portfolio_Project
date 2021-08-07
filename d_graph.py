# Course: CS261 - Data Structures
# Author: Kyle Brogdon
# Assignment: Assignment 6 Directed Graphs
# Description:

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a new vertex to the graph and then returns the number of vertices in the graph after the new addition
        """
        self.adj_matrix.append([])  # adds an empty list to the end of the matrix
        self.v_count += 1  # increment count
        for i in range(self.v_count):  # appends 0s to make the new vertex the appropriate length
            self.adj_matrix[self.v_count - 1].append(0)
        for i in range(self.v_count-1):  # adds a new index to all existing vertices
            self.adj_matrix[i].append(0)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=0) -> None:
        """
        Takes a src index (source), dst index (destination), and adds a positive integer weight to the graph.  If either
        index is out of range, or if src and dst are the same index, then the method performs no action.  If the edge
        already exists, then the weight is updated.
        """
        if src == dst:
            return
        if src < 0 or src > self.v_count-1:
            return
        if dst < 0 or dst > self.v_count-1:
            return
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Takes a src index (source), dst index (destination), and removes their edge from the graph.  If either
        index is out of range, or if there is no edge between the vertices, then this method does nothing.
        """
        if src == dst:
            return
        if src < 0 or src > self.v_count-1:
            return
        if dst < 0 or dst > self.v_count-1:
            return
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns a list containing the vertices of the graph
        """
        vertices = []
        for x in range(len(self.adj_matrix)):
            vertices.append(x)
        return vertices

    def get_edges(self) -> []:
        """
        Returns the edges in the graph as a tuple containing the incident vertices and the edge weight
        """
        edges = []
        for x in range(len(self.adj_matrix)):
            for y in range(len(self.adj_matrix[x])):
                if self.adj_matrix[x][y] > 0:  # if an edge exists
                    temp = (x, y, self.adj_matrix[x][y])  # store it as a tuple
                    edges.append(temp)  # append the tuple to the list
        return edges

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list containing a path, then traverses that path. If able to traverse the whole path, it is valid and
        this method returns True. Otherwise, it returns false
        """
        if path == []:
            return True
        for x in range(len(path)-1):
            if self.adj_matrix[path[x]][path[x+1]] == 0:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        if v_start not in self.get_vertices():
            return []
        if v_end is not None and v_end not in self.get_vertices():
            v_end = None
        visited_vertices = []
        stack = deque([v_start])
        while len(stack) > 0:
            temp = stack.pop()
            temp_list = []  # used to add vertices to the visited vertices list
            if temp not in visited_vertices:
                visited_vertices.append(temp)
            if temp == v_end:
                break
            for x in range(len(self.adj_matrix[temp])):  # iterate through reachable vertices
                if self.adj_matrix[temp][x] > 0:
                    temp_list.append(x)
                temp_list.sort(reverse=True)  # creates a descending order list of reachable vertices
            for x in range(len(temp_list)):
                if temp_list[x] not in visited_vertices:
                    stack.append(temp_list[x])  # append vertcies to stack so they are visited in ascending order
        return visited_vertices

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        if v_start not in self.get_vertices():
            return []
        if v_end is not None and v_end not in self.get_vertices():
            v_end = None
        visited_vertices = []
        queue = deque([v_start])
        while len(queue) > 0:
            temp = queue.pop()
            temp_list = []  # used to add vertices in lexicographocal order
            visited_vertices.append(temp)
            if temp == v_end:
                break
            for x in range(len(self.adj_matrix[temp])):  # iterate through reachable vertices
                if self.adj_matrix[temp] not in visited_vertices and self.adj_matrix[temp][x] > 0:
                    temp_list.append(x)
            temp_list.sort()  # creates a ascending list of reachable vertices
            for x in range(len(temp_list)):
                # if not visited yet and not already in queue for bfs
                if temp_list[x] not in visited_vertices and temp_list[x] not in queue:
                    # append vertcies to stack so they are visited in ascending lexicographical order
                    queue.appendleft(temp_list[x])
        return visited_vertices

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
