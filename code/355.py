class Twitter:
    from collections import deque
    from heapq import nlargest

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(lambda: deque(maxlen=10))
        self.timestamps = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)
        self.timestamps[tweetId] = self.time
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets[userId])
        for user in self.follows[userId]:
            feed.extend(self.tweets[user])
        return nlargest(10, feed, key=lambda x: self.timestamps[x])

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
