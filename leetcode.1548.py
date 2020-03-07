import collections
class MaxQueue:

    def __init__(self):
        self.queue = []
        self.sub_deque = collections.deque()

    def max_value(self) -> int:
        if not self.sub_deque:
            return -1
        else:
            return self.sub_deque[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.sub_deque and self.sub_deque[-1] < value:
            self.sub_deque.pop()
        self.sub_deque.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        else:
            tmp = self.queue.pop(0)
            if tmp == self.sub_deque[0]:
                self.sub_deque.popleft()
            return tmp



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()