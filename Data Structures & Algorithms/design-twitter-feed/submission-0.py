class Twitter:

    def __init__(self):
        self.time = 0
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        users = self.followees[userId] | {userId}
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweet = self.tweets[user][index]
                heap.append([time, tweet, user, index-1])
        heapq.heapify(heap)
        while heap and len(res) < 10:
            time, tweet, user, index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                next_time, next_tweet = self.tweets[user][index]
                heapq.heappush(heap, [next_time, next_tweet, user, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)