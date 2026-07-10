class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        reverse_stack = []
        while self.stack:
            item = self.stack.pop()
            reverse_stack.append(item)
        front_q = reverse_stack.pop()

        while reverse_stack:
            item = reverse_stack.pop()
            self.stack.append(item)
        return front_q

    def peek(self) -> int:
        reverse_stack = []
        while self.stack:
            item = self.stack.pop()
            reverse_stack.append(item)
        front_q = reverse_stack[-1]
        while reverse_stack:
            item = reverse_stack.pop()
            self.stack.append(item)
        return front_q

    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()