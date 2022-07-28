from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots = []
        for s, e in slots1:
            slots.append((s, 1))
            slots.append((e, -1))
        for s, e in slots2:
            slots.append((s, 1))
            slots.append((e, -1))

        slots.sort()

        pre = None
        level = 0
        for i in range(len(slots)):
            time, event = slots[i]
            level += event
            if level == 2:
                pre = time
            else:
                if pre != None and pre + duration <= time:
                    return [pre, pre + duration]
                else:
                    pre = None
        return []


if __name__ == "__main__":
    sol = Solution()
    slots1 = [[10, 50]]
    slots2 = [[1, 15], [17, 60]]
    duration = 15
    res = sol.minAvailableDuration(slots1, slots2, duration)
    print(res)
