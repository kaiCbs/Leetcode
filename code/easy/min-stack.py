import bisect
class MinStack:

    def __init__(self):
        self.stack = []
        self.sort = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        bisect.insort_left(self.sort,x)

    def pop(self) -> None:
        self.sort.remove(self.stack.pop())

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sort[0]