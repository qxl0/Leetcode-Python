"""
1340. Jump Game V
Hard

656

22

Add to List

Share
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.
"""
import collections
import sys
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if not arr or n == 0:
            return 0

        visited = set()
        maxNum = 0

        def DFS(curIndex, d, curLength, visited):
            nonlocal maxNum
            if curIndex in visited:
                return
            curLength += 1
            maxNum = max(maxNum, curLength)
            visited.add(curIndex)
            j = curIndex + 1
            while j < n and j <= curIndex + d and arr[j] < arr[curIndex]:
                DFS(j, d, curLength, visited)
                j += 1
            j = curIndex - 1
            while j >= 0 and j >= curIndex - d and arr[j] < arr[curIndex]:
                DFS(j, d, curLength, visited)
                j -= 1
            visited.remove(curIndex)

        for i in range(n):
            DFS(i, d, 0, visited)
        return maxNum


class Solution2:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if n == 0:
            return 0
        mixedList = [(arr[i], i) for i in range(n)]
        mixedList.sort()

        globalMax = 0
        dp = [1] * n
        for i in range(n):
            val, idx = mixedList[i]
            j = idx + 1
            while j < n and j <= idx + d and arr[j] < val:
                dp[idx] = max(dp[idx], 1 + dp[j])
                j += 1
            j = idx - 1
            while j >= 0 and j >= idx - d and arr[j] < val:
                dp[idx] = max(dp[idx], 1 + dp[j])
                j -= 1
            globalMax = max(globalMax, dp[idx])
        return globalMax


class Solution3:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if n == 0:
            return 0

        dp = [1] * n
        stack = []
        globalMax = 0
        #
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                curResult = 0

                j = idx + 1
                while j < i and j <= idx + d:
                    if arr[j] == arr[idx]:
                        break
                    curResult = max(curResult, dp[j])
                    j += 1
                dp[idx] = max(dp[idx], 1 + curResult)
                globalMax = max(globalMax, dp[idx])

                if i <= idx + d:
                    dp[i] = max(dp[i], 1 + dp[idx])
                    globalMax = max(globalMax, dp[idx])
            stack.append(i)

        # round 2
        while stack:
            idx = stack.pop()
            curResult = 0
            j = idx + 1
            while j < n and j <= idx + d:
                if arr[j] == arr[idx]:
                    break
                curResult = max(curResult, dp[j])
                j += 1
            dp[idx] = max(dp[idx], 1 + curResult)
            globalMax = max(globalMax, dp[idx])

        return globalMax


if __name__ == "__main__":
    s = Solution3()
    # arr = [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
    # d = 2
    arr = [7, 6, 5, 4, 3, 2, 1]
    d = 1
    res = s.maxJumps(arr, d)
    print("Ans is : ", res)
