from collections import Counter
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        results = []

        def dfs(num, target, cur, preStr, preVal, lastVal):
            if cur == len(num):
                if preVal == target:
                    results.append(preStr)
                return

            for i in range(cur + 1, len(num) + 1):
                curStr = num[cur:i]
                curVal = int(curStr)
                if cur != 0:
                    dfs(num, target, i, preStr + "+" + curStr, preVal + curVal, curVal)
                    dfs(num, target, i, preStr + "-" + curStr, preVal + curVal, -curVal)
                    dfs(
                        num,
                        target,
                        i,
                        preStr + "*" + curStr,
                        preVal - lastVal + lastVal * curVal,
                        lastVal * curVal,
                    )
                else:
                    dfs(num, target, i, curStr, curVal, curVal)

        dfs(num, target, 0, "", 0, 0)
        return results


if __name__ == "__main__":
    sol = Solution()
    s = "123"
    target = 6
    res = sol.addOperators(s, target)
    print(res)
