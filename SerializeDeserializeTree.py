class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(lst):
    return helper(lst, 0)


def helper(lst, i):
    if i >= len(lst) or not lst[i]:
        return None
    curr = TreeNode(lst[i]) if lst[i] else None
    curr.left = helper(lst, 2 * i + 1)
    curr.right = helper(lst, 2 * i + 2)

    return curr


class Codec:
    def serialize(self, root):
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append("#")

        vals = []
        helper(root)
        return " ".join(vals)

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()

        vals = iter(data.split())
        return helper()


if __name__ == "__main__":
    sol = Codec()
    # root = createTree([3, 9, 20, None, 13, 15, 7])
    # print(sol.serialize(root))
    data = "3 9 # 13 # # 20 15 # # 7 # #"
    res = sol.deserialize(data)
