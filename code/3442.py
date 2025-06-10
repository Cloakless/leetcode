class Solution:
    def maxDifference(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        odds = 0
        evens = 100
        for c in counter:
            num = counter[c]
            if num % 2 == 0:
                evens = min(evens, num)
            else:
                odds = max(odds, num)
        return odds - evens
      
