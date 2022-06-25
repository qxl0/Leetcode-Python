class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def countOfSmallerNumberII(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return []

        # mapping from nums to ids (ascending)
        sortedA = sorted(A)
        ids = {}
        maxId = 1
        for num in sortedA:
            if num not in ids:
                ids[num] = maxId
                maxId += 1

        def lowbit(idx):
            return idx & (-idx)

        def query(bit, idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= lowbit(idx)
            return s

        def update(bit, idx, delta):
            n = len(bit)
            while idx < n:
                bit[idx] += delta
                idx += lowbit(idx)

        # init bit
        bit = [0 for i in range(maxId)]

        ret = []
        for i, num in enumerate(A):
            id = ids[num]
            ret.append(query(bit, id - 1))
            update(bit, id, 1)

        return ret


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 7, 8, 5]

    res = sol.countOfSmallerNumberII(arr)

    print(res)
