class Node:
    def __init__(self, val: int, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}, next: {self.next}"

    def __str__(self) -> str:
        return str(self.val)

    def to_binary_tree(items: list[int]):
        """Create BT from list of values."""
        n = len(items)
        if n == 0:
            return None

        def inner(index: int = 0) -> Node:
            """Closure function using recursion bo build tree"""
            if n <= index or items[index] is None:
                return None

            node = Node(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()
