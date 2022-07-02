class Solution:
    def lengthLongestPath(self, input):

        maxPath = 0
        paths = [0]

        for subDir in input.splitlines():

            # getting the depth level of the current subpath
            level = subDir.count("\t")

            # increasing the size of the array of the parents subpaths, if needed
            if level >= len(paths):
                paths += [None]

            # updating the length of the current depth level
            paths[level] = (
                paths[level - 1] + len(subDir) - level + 1 if level > 0 else len(subDir)
            )

            # updating the maximum length
            if "." in subDir:
                maxPath = max(maxPath, paths[level])
        return maxPath


if __name__ == "__main__":
    sol = Solution()
    # input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    res = sol.lengthLongestPath(input)
    print("Ans is: ", res)
