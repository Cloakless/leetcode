class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        self.pointer = 0
        self.zero_index = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_index = self.pointer + 1
            self.nums.append(0)
        else:
            if self.nums[self.pointer] == 0:
                self.nums.append(num)
            else:
                self.nums.append(self.nums[self.pointer]*num)
        self.pointer += 1       

    def getProduct(self, k: int) -> int:
        if self.pointer - self.zero_index < k:
            return 0
        else:
            return self.nums[self.pointer] // max(1, self.nums[self.pointer - k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
