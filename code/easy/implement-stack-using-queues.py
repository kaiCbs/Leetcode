import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = queue.Queue(-1)

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.put(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(self.stack.qsize()-1):
            self.stack.put(self.stack.get())
        return self.stack.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(self.stack.qsize()-1):
            self.stack.put(self.stack.get())
        top = self.stack.get()
        self.stack.put(top)
        return top
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()