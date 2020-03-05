class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.input+self.output)

# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         self.stack.append(x)
        

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         temp = []
#         while self.stack:
#             temp.append(self.stack.pop())
#         top = temp.pop()
#         while temp:
#             self.stack.append(temp.pop())
#         return top

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         temp = []
#         while self.stack:
#             temp.append(self.stack.pop())
#         top = temp.pop()
#         self.stack.append(top)
#         while temp:
#             self.stack.append(temp.pop())
#         return top

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return not len(self.stack)