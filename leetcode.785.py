from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for i in graph[node]:
                        if i not in color:
                            stack.append(i)
                            color[i] = color[node] ^ 1
                        elif color[i] == color[node]:
                            return False
        return True