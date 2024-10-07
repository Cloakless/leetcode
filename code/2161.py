class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        below = []
        above = []
        pivot_count = 0
        for num in nums:
            if num < pivot:
                below.append(num)
            elif num > pivot:
                above.append(num)
            else:
                pivot_count += 1
        return below + [pivot] * pivot_count + above
