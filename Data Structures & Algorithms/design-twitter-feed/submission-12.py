import heapq
from collections import defaultdict

class Twitter:
    def __init__(self) -> None:
        self.ts = 0
        # userId -> list of (timestamp, tweetId), in post order (oldest -> newest)
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        # userId -> set of followee ids
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.ts, tweetId))
        self.ts += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # A user always sees their own tweets.
        sources = self.following[userId] | {userId}

        # Seed a max-heap (negate ts) with each source's most recent tweet.
        # Heap entries: (-ts, tweetId, ownerId, index_of_that_tweet)
        heap: list[tuple[int, int, int, int]] = []
        for uid in sources:
            user_tweets = self.tweets[uid]
            if user_tweets:
                i = len(user_tweets) - 1        # newest tweet
                ts, tid = user_tweets[i]
                heapq.heappush(heap, (-ts, tid, uid, i))

        feed: list[int] = []
        while heap and len(feed) < 10:
            _, tid, uid, i = heapq.heappop(heap)
            feed.append(tid)
            if i > 0:                            # push this source's next-older tweet
                ts, ntid = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-ts, ntid, uid, i - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)