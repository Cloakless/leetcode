class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        before_guards = 10000000
        after_guards = 10000000
        before = 0
        after = n
        last_increase = [0] * n
        next_decrease = [n-1] * n
        for i in range(1, n):
            if security[i] > security[i-1]:
                last_increase[i] = i
            else:
                last_increase[i] = last_increase[i-1]
            if security[n-1-i] > security[n-i]:
                next_decrease[n-i-1] = n-i-1
            else:
                next_decrease[n-i-1] = next_decrease[n-i]
        ans = []
        for i in range(time, n-time):
            if last_increase[i] <= i - time and next_decrease[i] >= i + time:
                ans.append(i)
        return ans
