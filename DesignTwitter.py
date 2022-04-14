"""
355. Design Twitter
Medium

1961

272

Add to List

Share
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
"""

from collections import Counter, deque
import datetime
from filecmp import cmp
import heapq
import math
import pstats
import random
from typing import List, Optional


class Twitter:
    def __init__(self):
        self.follows = {}
        self.post = {}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.post:
            self.post[userId] = []
        self.post[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # get all its follows
        if userId not in self.follows:
            self.follows[userId] = []
        follows = self.follows[userId][:]
        follows.append(userId)
        heap = []
        for f in follows:
            if f not in self.post:
                continue
            for da, tw in self.post[f]:
                heapq.heappush(heap, (-da, tw))
        i = 0
        while heap and i < 10:
            res.append(heapq.heappop(heap)[1])
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = []
        if followeeId in self.follows[followerId]:
            return
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    # twitter.postTweet(1, 5)
    # twitter.getNewsFeed(1)
    # twitter.follow(1, 2)
    # twitter.postTweet(2, 6)
    # res = twitter.getNewsFeed(1)
    # twitter.postTweet(1, 1)
    # twitter.getNewsFeed(1)
    # twitter.follow(2, 1)
    # twitter.getNewsFeed(2)
    # twitter.unfollow(2, 1)
    twitter.postTweet(2, 5)
    twitter.follow(1, 2)
    twitter.follow(1, 2)
    twitter.getNewsFeed(1)
    res = twitter.getNewsFeed(2)
    print(res)
