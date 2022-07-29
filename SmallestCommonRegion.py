from typing import List


class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        parent = {}
        for region in regions:
            for i in range(1, len(region)):
                parent[region[i]] = region[0]
        chain = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            chain.add(region1)
        while region2 not in chain:
            region2 = parent[region2]
        return region2


if __name__ == "__main__":
    sol = Solution()
    regions = (
        [
            ["Earth", "North America", "South America"],
            ["North America", "United States", "Canada"],
            ["United States", "New York", "Boston"],
            ["Canada", "Ontario", "Quebec"],
            ["South America", "Brazil"],
        ],
    )
    region1 = ("Quebec",)
    region2 = "New York"
    res = sol.findSmallestRegion(regions, region1, region2)
    print(res)
