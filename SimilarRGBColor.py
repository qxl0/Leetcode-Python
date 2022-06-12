class Solution:
    def similarRGB(self, color: str) -> str:
        result = []

        def closest(ss):
            m = [
                "00",
                "11",
                "22",
                "33",
                "44",
                "55",
                "66",
                "77",
                "88",
                "99",
                "aa",
                "bb",
                "cc",
                "dd",
                "ee",
                "ff",
            ]
            d = float("inf")
            idx = -1
            for i in range(len(m)):
                dist = abs(int(ss, 16) - int(m[i], 16))
                # print(i, m[i], dist)
                if dist < d:
                    d = dist
                    idx = i
            # print(m[idx], d)
            return m[idx]

        for i in range(1, len(color), 2):
            result.append(closest(color[i : i + 2]))
        return "#" + "".join(result)


if __name__ == "__main__":
    sol = Solution()
    color = "#09f166"
    res = sol.similarRGB(color)
    print(res)
