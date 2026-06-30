class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        h = [[-1*count[x], x] for x in count]
        print(h)
        heapq.heapify(h)
        q = deque([[0,"Idle"]]*(n+1))
        q_non_idle_count = 0
        print(q)
        ans = 0
        res = []

        while h or q_non_idle_count:
            available = q.popleft()
            if available[1] != "Idle":
                heapq.heappush(h, available)
                q_non_idle_count -= 1
            if h:
                curr = heapq.heappop(h)
                curr[0] += 1
                if curr[0] != 0:
                    q.append(curr)
                    q_non_idle_count += 1
                else:
                    q.append([0,"Idle"])
            else:
                q.append([0,"Idle"])
            # print(f"{curr=} {h=} {q=}")
            ans += 1
            # res.append
        
        
        return ans


        