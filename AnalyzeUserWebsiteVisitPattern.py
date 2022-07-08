from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:

        packed_tuple = zip(
            timestamp, username, website
        )  # ---> [(3, 'joe', 'career'),....]
        sorted_packed_tuple = sorted(
            packed_tuple
        )  # sort by timestamp, as it didn't say timestamp is sorted array
        # By default tuple always being sorted by the first item

        mapping = defaultdict(list)
        for (
            t,
            u,
            w,
        ) in (
            sorted_packed_tuple
        ):  # joe: ['home', 'about', 'career']  websites in list are in ascending timestamp order
            mapping[u].append(w)

        counter_dict = defaultdict(int)  # use a dict for counting
        for website_list in mapping.values():
            combs = set(
                combinations(website_list, 3)
            )  # size of combination is set to 3, for details see bottom
            for comb in combs:
                counter_dict[
                    comb
                ] += 1  # Tuple as key, counter as value,  e.g. ('home', 'about', 'career') : 2

        sorted_counter_dict = sorted(
            counter_dict, key=lambda x: (-counter_dict[x], x)
        )  # sort descending by value, then lexicographically
        return sorted_counter_dict[0]


if __name__ == "__main__":
    sol = Solution()
    username = [
        "joe",
        "joe",
        "joe",
        "james",
        "james",
        "james",
        "james",
        "mary",
        "mary",
        "mary",
    ]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = [
        "home",
        "about",
        "career",
        "home",
        "cart",
        "maps",
        "home",
        "home",
        "about",
        "career",
    ]
    res = sol.mostVisitedPattern(username, timestamp, website)
    print("Ans is: ", res)
