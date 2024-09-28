class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.n = 0
        self.start = 1
        self.end = 0
        self.items = [None] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.start -= 1
        self.n += 1
        self.start %= self.k
        self.items[self.start] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end += 1
        self.n += 1
        self.end %= self.k
        self.items[self.end] = value
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start += 1
        self.n -= 1
        self.start %= self.k
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end -= 1
        self.end %= self.k
        self.n -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.start]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[self.end]
        

    def isEmpty(self) -> bool:
        return self.n == 0
        

    def isFull(self) -> bool:
        return self.n == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
