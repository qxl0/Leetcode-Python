from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.stream = [None] * (n + 2)

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        if id == self.ptr:
            while self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[id : self.ptr]
        return []


if __name__ == "__main__":
    os = OrderedStream(5)
    os.insert(1, "aaaaa")
    # Inserts (1, "aaaaa"), returns ["aaaaa"].
    os.insert(3, "ccccc")
    # Inserts (3, "ccccc"), returns [].
    os.insert(2, "bbbbb")
    # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    os.insert(5, "eeeee")
    # Inserts (5, "eeeee"), returns [].
    os.insert(4, "ddddd")
    # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
