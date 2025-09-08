class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 0
        while True:
            i += 1
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]
