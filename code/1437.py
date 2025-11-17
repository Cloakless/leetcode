class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_time = 10000000
        for num in nums:
            if num == 1:
                if last_time < k + 1:
                    return False
                last_time = 0
            last_time += 1
        return True
