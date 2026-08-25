class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # 0 - 1
        # 1 - 0, 2
        # 2 - 1
        # 3 - 4
        # 4 - 3
        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count





        
        