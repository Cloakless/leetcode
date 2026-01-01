class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tot = 0
        for digit in digits:
            tot *= 10
            tot += digit
        tot += 1
        tot = str(tot)
        ans = []
        for idx in range(len(tot)):
            ans.append(int(tot[idx]))
        return ans
