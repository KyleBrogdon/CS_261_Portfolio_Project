# Course: CS261 - Data Structures
# Author: Kyle Brogdon
# Assignment: Assignment 6 undirected Graphs
# Description:

import heapq
from collections import deque

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        if v in self.adj_list:
            return
        else:
            self.adj_list[v] = []

    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if u == v:  # if the vertices are the same
            return
        if u not in self.adj_list:  # check if the key u exists, if not, create it
            self.add_vertex(u)
        if v not in self.adj_list:  # check if the key v exists, if not, create it
            self.add_vertex(v)
        if v in self.adj_list[u] and u in self.adj_list[v]:  # if an edge already exists, return
            return
        else:  # otherwise, create an edge between the vertices
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        if u not in self.adj_list:  # if u is not a vertex then no edge can exist
            return
        if v not in self.adj_list:  # if v is not a vertex then no edge can exist
            return
        if u not in self.adj_list[v] and v not in self.adj_list[u]:  # if an edge does not exist
            return
        if self.adj_list[v] is self.adj_list[u]:
            return
        else:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v not in self.adj_list:
            return
        temp_list = []
        for key in self.adj_list.keys():  # iterate through the dictionary and store keys as lists
            temp_list.append(key)
        for x in range(len(self.adj_list)):  # iterate through and remove all edges from v to other vertices
            self.remove_edge(temp_list[x], v)
        self.adj_list.pop(v, None)  # remove v



    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        temp_list = []
        for key in self.adj_list.keys():  # iterate through the dictionary and store keys as lists
            temp_list.append(key)
        return temp_list

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        temp_list = []
        edge_list = []
        for key, value in self.adj_list.items():  # iterate through the dictionary and store keys as lists
            for x in range (len(self.adj_list[key])):
                temp = [key, self.adj_list[key][x]]
                if temp not in temp_list and temp.reverse() not in temp_list:
                    temp_list.append(temp)
        for x in range(len(temp_list)):
            edge_list.append(tuple(temp_list[x]))
        return edge_list
        

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        stack = deque()
        for x in range(len(path)-1, -1, -1):
            stack.append(path[x])
        if len(stack) == 1:
            temp = stack.pop()
            if temp not in self.adj_list:
                return False
        while len(stack) > 1:
            reachable = set()
            temp = stack.pop()
            for i in range (len(self.adj_list[temp])):
                reachable.add(self.adj_list[temp][i])
            if stack[len(stack) - 1] not in reachable:  # if the next vertex is not reachable
                return False
        return True

       

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        if v_start not in self.adj_list:
            return []
        if v_end is not None and v_end not in self.adj_list:
            v_end = None
        visited_vertices = []
        stack = deque(v_start)
        while len(stack) > 0:
            temp = stack.pop()
            temp_list = []  # used to add vertices in reverse lexicographocal order
            if temp not in visited_vertices:
                visited_vertices.append(temp)
            if temp == v_end:
                break
            for x in range(len(self.adj_list[temp])):  # iterate through reachable vertices
                temp_list.append(self.adj_list[temp][x])
                temp_list.sort(reverse=True)  # creates a descending order list of reachable vertices
            for x in range(len(temp_list)):
                if temp_list[x] not in visited_vertices:
                    stack.append(temp_list[x])  # append vertcies to stack so they are visited in ascending lexicographical order
        return visited_vertices



    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        if v_start not in self.adj_list:
            return []
        if v_end is not None and v_end not in self.adj_list:
            v_end = None
        visited_vertices = []
        queue = deque(v_start)
        while len(queue) > 0:
            temp = queue.pop()
            temp_list = []  # used to add vertices in lexicographocal order
            visited_vertices.append(temp)
            if temp == v_end:
                break
            for x in range(len(self.adj_list[temp])):  # iterate through reachable vertices
                if self.adj_list[temp][x] not in visited_vertices:
                    temp_list.append(self.adj_list[temp][x])
            temp_list.sort()  # creates a ascending list of reachable vertices
            for x in range(len(temp_list)):
                # if not visited yet and not already in queue for bfs
                if temp_list[x] not in visited_vertices and temp_list[x] not in queue:
                    # append vertcies to stack so they are visited in ascending lexicographical order
                    queue.appendleft(temp_list[x])
        return visited_vertices

    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
        unvisited_vertices = self.get_vertices()
        connected_components = 0
        while len(unvisited_vertices) > 0:
            visited_vertices = self.dfs(unvisited_vertices[0])
            for x in range(len(visited_vertices)):
                unvisited_vertices.remove(visited_vertices[x])
            connected_components += 1
        return connected_components


    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        unsearched_vertices = self.get_vertices()  # creates a list of all vertices
        parent = dict()
        for i in range(len(unsearched_vertices)):  # creates a dictionary to store the parent values of vertices
            parent[unsearched_vertices[i]] = None
        while len(unsearched_vertices) > 0:  # perform a DFS on each vertex using helper method
            has_cycle = self.has_cycle_helper(unsearched_vertices[0], parent)  # store the true or false value
            if has_cycle is True:  # if a cycle exists, break
                return True
            unsearched_vertices.remove(unsearched_vertices[0])  # if a cycle doesn't exist, remove vertex and continue
        return False  # no cycles exist


    def has_cycle_helper(self, v, parent):
        """
        Helper method that takes a vertex, and the list of parent vertices, does a DFS starting from v and returns true
        if a cycle exists from v
        """
        visited_vertices = []
        stack = deque(v)
        while len(stack) > 0:
            temp = stack.pop()
            temp_list = []  # used to add vertices in reverse lexicographocal order
            if temp not in visited_vertices:
                visited_vertices.append(temp)
            for x in range(len(self.adj_list[temp])):  # iterate through reachable vertices
                temp_list.append(self.adj_list[temp][x])
                temp_list.sort(reverse=True)  # creates a descending order list of reachable vertices
            for x in range(len(temp_list)):
                if temp_list[x] not in visited_vertices and temp_list[x] not in stack:
                    # append vertices to stack so they are visited in ascending lexicographical order
                    stack.append(temp_list[x])
                    parent[temp_list[x]] = temp  # update parent values for the vertices we just added
                    # if a vertex was visited and it's not the parent vertex, then a cycle must exist, return True
                if temp_list[x] in visited_vertices and temp_list[x] != parent[temp]:
                    return True
        return False  # cycle does not exist from v

   


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)
    test = UndirectedGraph


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
