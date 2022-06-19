class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        current_possible_length = 0
        current_sum = 0
        for i in s[::-1]:
            if i == "0":
                current_possible_length += 1

            elif current_sum + (1 << current_possible_length) <= k:
                current_sum += 1 << current_possible_length
                current_possible_length += 1

        return current_possible_length


if __name__ == "__main__":
    sol = Solution()
    s = "00101001"
    k = 2
    res = sol.longestSubsequence(s, k)
    print("result is: ", res)
