class Solution:
    def maxScore(self, s: str) -> int:
        zeros = []
        ones = []
        num0, num1 = 0, 0
        n = len(s)

        for i in range(n):
            if s[i] == '0':
                num0 += 1
            if s[n-i-1] == '1':
                num1 += 1
            zeros.append(num0)
            ones.append(num1)
        ones = ones[::-1]
        best = 0
        for i in range(n-1):
            best = max(best, zeros[i] + ones[i+1])
        return best
