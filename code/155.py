class MinStack:

    def __init__(self):
        self.pointer = 0
        self.n = 0
        self.stack = [(float('inf'), float('inf'))]
        

    def push(self, val: int) -> None:
        self.pointer += 1
        if self.pointer <= self.n:
            self.stack[self.pointer] = (val, min(val, self.stack[self.pointer-1][1]))
        else:
            self.stack.append((val, min(val, self.stack[self.pointer-1][1])))
            self.n += 1
        

    def pop(self) -> None:
        ans = self.stack[self.pointer][0]
        self.pointer -= 1
        return ans
        

    def top(self) -> int:
        return self.stack[self.pointer][0]
        

    def getMin(self) -> int:
        return self.stack[self.pointer][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
