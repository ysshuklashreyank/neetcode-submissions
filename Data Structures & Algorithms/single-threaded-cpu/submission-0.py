class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        lenn = len(tasks)
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        h = []
        # print(tasks)

        j = 0
        exec_time = tasks[0][0]
        while h or j < lenn:
            # currET = exec_time
            # j = i
            while j < lenn and  tasks[j][0] <= exec_time:
                heapq.heappush(h, [tasks[j][1], tasks[j][2], tasks[j][0]])
                j += 1
            # print(f"{exec_time=} {h=} {j=}")
            if h:
                todoTask = heapq.heappop(h)
                res.append(todoTask[1])
                exec_time += todoTask[0]
                # print(f"{todoTask=} {exec_time=} \n")
            else:
                # cpu will idle till next enque time
                exec_time = tasks[j][0]
        return res








