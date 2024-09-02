class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1

        def hasEnough(d):
            curr = 0
            tot = 0
            for i in range(n):
                if bloomDay[i] <= d:
                    curr += 1
                else:
                    curr = 0
                if curr == k:
                    tot += 1
                    curr = 0
            return tot >= m

        left = 0
        right = max(bloomDay)
        while left < right - 1:
            test = int((left + right)/2)
            test_result = hasEnough(test)
            if test_result:
                right = test
            else:
                left = test

        return right
        
