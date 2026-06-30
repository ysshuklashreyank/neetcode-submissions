class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[0]*n for _ in range(n)]
        for a, b in edges:
            adj[a][b] = 1
            adj[b][a] = 1

        path = set()
        global count
        count = 0

        def dfs(curr):
            print(f"{curr=} {path=}")
            global count
            count += 1
            if curr in path:
                return False
            path.add(curr)
            # for neigh in adj[curr]:
            #     if dfs(neigh) == False:
            #         return False
            for col in range(n):
                if adj[curr][col] == 1:
                    adj[curr][col] = 0
                    adj[col][curr] = 0
                    if dfs(col) == False:
                        return False
                    
            path.remove(curr)
            # adj[curr] = [0]
        

            return True

        # for node in range(n):
        #     if dfs(node) == False:
        #         return False

        if dfs(0) == False:
            return False
        if count != n:
            return False
        return True

        