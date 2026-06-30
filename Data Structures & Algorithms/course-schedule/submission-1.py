class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visited = set() 
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        

        def dfs(curr, start):
            # visited.add(curr)
            for neigh in adj[curr]:
                if neigh == start:
                    return True
                res = dfs(neigh, start)
                if res:
                    return True 





        for start in range(numCourses):
            visited = set()
            if dfs(start, start):
                return False
        return True

        

        