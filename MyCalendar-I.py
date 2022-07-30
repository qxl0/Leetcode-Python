class MyCalendar:
    def __init__(self):
        pass

    def book(self, start, end):
        pass


if __name__ == "__main__":
    sol = MyCalendar()
    sol.book(47, 50)
    sol.book(33, 41)
    sol.book(39, 45)
    sol.book(33, 42)
    sol.book(25, 32)
    sol.book(26, 35)
    sol.book(19, 25)
    sol.book(47, 50)
    sol.book(3, 8)
    sol.book(8, 13)
    res = sol.book(18, 27)
    print(res)
