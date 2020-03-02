class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        i = len(self.list)
        self.list.append(x)
        while i:
            i -= 1
            self.list.append(self.list.pop(0))


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.list.pop(0) if self.list else None


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.list[0] if self.list else None


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.list else True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()