class Solution:
    def bestClosingTime(self, customers: str) -> int:
        hours = customers.count('Y')
        zeros = 0
        best = hours
        ans = 0
        for i in range(len(customers)):
            if customers[i] == 'Y':
                hours -= 1
            else:
                zeros += 1
            cand = hours + zeros
            if cand < best:
                ans = i + 1
                best = cand
        return ans
