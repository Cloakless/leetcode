class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.n = len(nums)
        

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        new_array = [x for x in self.original]
        for i in range(self.n):
            target = random.randint(i, self.n-1)
            new_array[i], new_array[target] = new_array[target], new_array[i]
        return new_array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
