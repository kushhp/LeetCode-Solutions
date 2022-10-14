class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeToNeighbors = {}
        components = 0
        visited = set()
        for i in range(n):
            nodeToNeighbors[i] = []
        for node, neighbhor in edges:
            nodeToNeighbors[node].append(neighbhor)
            nodeToNeighbors[neighbhor].append(node)
        
        for node in nodeToNeighbors:
            if node not in visited:
                self.dfs(node, nodeToNeighbors, visited)
                components += 1
        return components
    
    def dfs(self, node, nodeToNeighbors, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in nodeToNeighbors[node]:
            self.dfs(neighbor, nodeToNeighbors, visited)
        return
        