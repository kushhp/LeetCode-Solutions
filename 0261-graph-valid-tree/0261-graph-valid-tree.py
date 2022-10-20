class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False
        adjList = {}
        visited = set()

        for i in range(n): 
            adjList[i] = []
        for start, end in edges: 
            adjList[start].append(end)
            adjList[end].append(start)
            
        self.dfs(0, adjList, visited)
        return len(visited) == n
        
    def dfs(self, node, adjList, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adjList[node]:
            self.dfs(neighbor, adjList, visited)
        return
            