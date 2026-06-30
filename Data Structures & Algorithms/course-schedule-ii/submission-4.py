class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = set() 
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)


        def cycle(curr):
            if curr in path:
                return True
            path.add(curr)
            # if curr not in res:
            #     res.append(curr)
            for neigh in adj[curr]:
                if cycle(neigh):
                    return True
            path.remove(curr)
            adj[curr] = []
            return False

        # res = []
        for course in range(numCourses):
            if cycle(course):
                return []

        visited = set()
        adj = defaultdict(list)
        degree = defaultdict(int)
        for a, b in prerequisites:
            adj[b].append(a)
            degree[a] += 1
        q = deque()
        res = []

        def bfs(start):
            print(f"doing bfs for {start=}")
            q.append(start)
            while q:
                curr = q.popleft()
                # visited.add(curr)
                res.append(curr)

                for neigh in adj[curr]:
                    if degree[neigh] <= 1:
                        q.append(neigh)
                    else:
                        degree[neigh] -= 1

        while len(res) != numCourses:
            for i in range(numCourses):
                # print(i)
                if i not in degree:
                    bfs(i)
                elif degree[i] == 0:
                    bfs(i)

        # print(degree, adj)
        return res
        