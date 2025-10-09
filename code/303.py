class NumArray:

    def __init__(self, nums: List[int]):
        self.prefs = []
        self.n = len(nums)
        base = 0
        for num in nums:
            base += num
            self.prefs.append(base)

    def sumRange(self, left: int, right: int) -> int:
        left, right = max(0, left), min(right, self.n - 1)
        pr = self.prefs[right]
        if left == 0:
            pl = 0
        else:
            pl = self.prefs[left-1]
        return pr - pl



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
