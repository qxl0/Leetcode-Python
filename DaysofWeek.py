class Solution:
    def dayOfTheWeek(self, d, m, y):
        days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        if m < 3:
            m += 12
            y -= 1
        c, y = y / 100, y % 100
        w = (c / 4 - 2 * c + y + y / 4 + 13 * (m + 1) / 5 + d - 1) % 7
        return days[int(w)]


if __name__ == "__main__":
    sol = Solution()
    y = 2022
    m = 6
    d = 15
    res = sol.dayOfTheWeek(d, m, y)
    print(res)
