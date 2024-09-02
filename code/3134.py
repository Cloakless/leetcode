class Solution:
    from collections import defaultdict
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        def median(k):
            if k % 2 == 0:
                return int(k / 2)
            else:
                return int((k + 1) / 2)
        def count_arrs(x):
            # Count the number of subarrays which have at most x distinct elements
            counter = defaultdict(int)
            l = 0
            r = 0
            num_unique = 1
            counter[nums[0]] = 1
            arrs = 1
            while l < n:
                # Try advance R
                if r < n - 1 and (num_unique < x or counter[nums[r+1]] != 0):
                    arrs += 1
                    r += 1
                    if counter[nums[r]] == 0:
                        num_unique += 1
                    counter[nums[r]] += 1
                # Else advance L
                else:
                    l += 1
                    if l > n - 1:
                        break
                    counter[nums[l-1]] -= 1
                    if l > r:
                        r = l
                        counter[nums[l-1]] = 0
                        counter[nums[l]] = 1
                        num_unique = 1
                    elif counter[nums[l-1]] == 0:
                        num_unique -= 1
                    arrs += (r - l) + 1
            return arrs

        num_distinct = n * (n + 1) // 2
        target = median(num_distinct)
        lower = 1
        upper = len(set(nums))
        while lower < upper - 1:
            mid = int((lower + upper) // 2)
            val = count_arrs(mid)
            if val > target:
                upper = mid
            elif val == target:
                return mid
            else:
                lower = mid
        if count_arrs(lower) >= target:
            return lower
        else:
            return upper
