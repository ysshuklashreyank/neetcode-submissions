class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set() 
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        

        def cycle(curr):
            if curr in path:
                return True
            path.add(curr)
            for neigh in adj[curr]:
                if cycle(neigh):
                    return True
            path.remove(curr)
            adj[curr] = []
            return False

        for start in range(numCourses):
            visited = set()
            if cycle(start):
                return False
        return True

        

        