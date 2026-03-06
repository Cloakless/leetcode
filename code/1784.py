class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = []
        for i, c in enumerate(s):
            if c == '1':
                ones.append(i)
        if not ones:
            return True
        for j in range(len(ones) - 1):
            if ones[j] != ones[j+1] - 1:
                return False
        return True
