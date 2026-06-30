"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newNode = Node(node.val)

        visited = set()
        nodesMap = dict()
        nodesMap[node] = newNode

        def dfs(node, newNode):
            for neigh in node.neighbors:
                if (node, neigh) not in visited:
                    visited.add((node,neigh))
                    if neigh not in nodesMap:
                        newNeigh = Node(neigh.val)
                        nodesMap[neigh] = newNeigh
                    else:
                        newNeigh = nodesMap[neigh]

                    newNode.neighbors.append(newNeigh)
                    # print(f"{node.val=} {neigh.val=} {[x.val for x in node.neighbors]} {newNode.val=} {newNeigh.val=} {[x.val for x in newNode.neighbors]}\n")
                    dfs(neigh, newNeigh)
        dfs(node, newNode)
        return newNode
