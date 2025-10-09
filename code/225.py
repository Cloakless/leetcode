class MyStack:
    from collections import deque

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.n = 0
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.n += 1
        

    def pop(self) -> int:
        for i in range(self.n-1):
            self.q2.append(self.q1.popleft())
        ans = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        self.n -= 1
        return ans

        

    def top(self) -> int:
        for i in range(self.n-1):
            self.q2.append(self.q1.popleft())
        ans = self.q1.popleft()
        self.q2.append(ans)
        self.q1, self.q2 = self.q2, self.q1
        return ans
        

    def empty(self) -> bool:
        return self.n == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
