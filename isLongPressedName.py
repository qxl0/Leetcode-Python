class Solution:
    def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)


if __name__ == "__main__":
    sol = Solution()
    name = "alex"
    typed = "aaleex"
    res = sol.isLongPressedName(name, typed)
    print(res)
