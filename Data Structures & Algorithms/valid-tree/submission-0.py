class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edges = [[0,1],[0,2],[0,3],[1,4]]
        # 0 -> 1, 2, 3
        # 1 -> 0, 4
        # 2 -> 0
        # 3 -> 0
        # 4 -> 1
        adj = {i:[] for i in range(n)}
        for lis in edges:
            n1 = lis[0]
            n2 = lis[1]
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)

        
        




        