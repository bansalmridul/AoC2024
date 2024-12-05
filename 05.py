import copy
import math
import random
from collections import defaultdict

# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # set of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if i in visited and visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)
        # print(f"inserted: {v}")

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = {key: False for key in self.V}
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in list(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        return stack


def part1(test=False):
    if test:
        fn = f"input{__file__[:-3]}-t.txt"
    else:
        fn = f"input{__file__[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    ret = 0
    v_map = defaultdict(list)
    v_set = set()
    ind = -1
    for i, line in enumerate(arrt):
        line = line.strip()
        if len(line) <= 1:
            ind = i
            break
        vals = [int(x) for x in list(filter(bool, line.split("|")))]
        v_map[vals[0]].append(vals[1])
        v_set.add(vals[0])
        v_set.add(vals[1])

    for line in arrt[ind + 1 :]:
        vals = [int(x) for x in list(filter(bool, line.split(",")))]
        g = Graph(vals)
        g.graph = {key: v_map[key] for key in vals}
        stack = g.topologicalSort()
        if stack == vals:
            ret += vals[len(vals) // 2]
    print(ret)


def part2(test=False):
    if test:
        fn = f"input{__file__[:-3]}-t.txt"
    else:
        fn = f"input{__file__[:-3]}.txt"
    file1 = open(fn, "r+")
    arrt = file1.readlines()
    ret = 0
    v_map = defaultdict(list)
    v_set = set()
    ind = -1
    for i, line in enumerate(arrt):
        line = line.strip()
        if len(line) <= 1:
            ind = i
            break
        vals = [int(x) for x in list(filter(bool, line.split("|")))]
        v_map[vals[0]].append(vals[1])
        v_set.add(vals[0])
        v_set.add(vals[1])

    for line in arrt[ind + 1 :]:
        vals = [int(x) for x in list(filter(bool, line.split(",")))]
        g = Graph(vals)
        g.graph = {key: v_map[key] for key in vals}
        stack = g.topologicalSort()
        if stack != vals:
            ret += stack[len(vals) // 2]
    print(ret)


if __name__ == "__main__":
    part1()
    part2()
