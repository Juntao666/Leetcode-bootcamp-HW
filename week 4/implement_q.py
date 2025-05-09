class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 0:
            curr = self.stack1.pop()
            self.stack2.append(curr)
        popped = self.stack2.pop()
        while len(self.stack2) > 0:
            curr = self.stack2.pop()
            self.stack1.append(curr)
        return popped

    def peek(self) -> int:
        while len(self.stack1) > 0:
            curr = self.stack1.pop()
            self.stack2.append(curr)
        peeked = self.stack2[-1]
        while len(self.stack2) > 0:
            curr = self.stack2.pop()
            self.stack1.append(curr)
        return peeked

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()