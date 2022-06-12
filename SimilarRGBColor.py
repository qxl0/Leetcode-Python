class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        result = []

        for i in range(1, len(color), 2):
            result.append(self.getClosest(color[i : i + 2]))

        return "#" + "".join(result)

    def getClosest(self, ss):
        hexcolor = [
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

        distances = []

        for color in hexcolor:
            dist = abs(int(ss, 16) - int(color, 16))
            distances.append(dist)

        return hexcolor[distances.index(min(distances))]


if __name__ == "__main__":
    sol = Solution()
    color = "#09f166"
    res = sol.similarRGB(color)
    print(res)
