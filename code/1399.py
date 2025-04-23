class Solution:
    def countLargestGroup(self, n: int) -> int:
        dig_sum = defaultdict(int)
        def dsum(k):
            tot = 0
            for c in str(k):
                tot += int(c)
            return tot
        for i in range(1, n+1):
            dig_sum[dsum(i)] += 1

        lst = []
        for d in dig_sum:
            lst.append(dig_sum[d])
        lst.sort()
        return lst.count(lst[-1])
