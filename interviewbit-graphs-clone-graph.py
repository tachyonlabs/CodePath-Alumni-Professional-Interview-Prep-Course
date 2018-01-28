# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        cloned_nodes = {}
        checked = {}
        cloned_start_node = None
        queue = deque([node])
        # first a BFS to clone all the nodes but with empty neighbors lists
        while queue:
            current = queue.popleft()
            cloned_nodes[current.label] = UndirectedGraphNode(current.label)
            if not cloned_start_node:
                cloned_start_node = cloned_nodes[current.label]
            checked[current] = 1
            for neighbor in current.neighbors:
                if neighbor not in checked and neighbor not in queue:
                    queue.append(neighbor)

        # then another round to fill in the neighbors lists
        checked = {}
        queue = deque([node])
        while queue:
            current = queue.popleft()
            checked[current] = 1
            for neighbor in current.neighbors:
                cloned_nodes[current.label].neighbors.append(cloned_nodes[neighbor.label])
                if neighbor not in checked and neighbor not in queue:
                    queue.append(neighbor)

        return cloned_start_node
