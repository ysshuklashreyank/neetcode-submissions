class Twitter:

    def __init__(self):
        self.time = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # if len(self.tweets[userId]) > 10:
        #     heapq.heappop(self.tweets[userId])
        # heapq.heappush(self.tweets[userId], [self.time, tweetId])

        self.tweets[userId].append([self.time, tweetId])
        self.tweets[userId].sort(reverse=True)
        if len(self.tweets[userId]) > 10:
            self.tweets[userId] = self.tweets[userId][:10]

        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        users = []
        for u in self.followers[userId]:
            if self.tweets[u]:
                users.append(u)
        if self.tweets[userId]:
            users.append(userId)
        if not users:
            return res

        print(f"{users=}")
        print(f"{self.tweets=}")

        

        tweetCount = 0
        # k = [0]*len(users)
        k = defaultdict(int)
        while tweetCount < 10:
            maxx = [-1,-1]
            maxUser = 0
            # for i in range(len(users)):
            #     if k[i] < len(tweets[users[i]]) and tweets[users[i]][k[i]] > maxx[0]:
            #         maxx = tweets[users[i]][k[i]]
            #         maxUser = i
            for uid in users:
                if self.tweets[uid][k[uid]][0] > maxx[0]:
                    maxx = self.tweets[uid][k[uid]]
                    maxUser = uid
            res.append(maxx[1])
            print(f"{res=}")

            tweetCount += 1
            k[maxUser] += 1
            if k[maxUser] >= len(self.tweets[maxUser]):
                users.remove(maxUser)
            if not users:
                print("returing now \n")
                return res
        
        print("returing now \n")
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)