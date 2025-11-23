class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        zeros, ones, twos = [], [], []
        for num in nums:
            if num % 3 == 0:
                zeros.append(num)
            elif num % 3 == 1:
                ones.append(num)
            else:
                twos.append(num)
        ones.sort()
        twos.sort()
        best = sum(nums)
        if best % 3 == 0:
            return best
        elif best % 3 == 1:
            if ones == []:
                if len(twos) < 2:
                    return sum(zeros)
                else:
                    return best - twos[0] - twos[1]
            other_cand = 0
            if len(twos) >= 2:
                other_cand = best - twos[0] - twos[1]
            return max(best - ones[0], other_cand)
        else:
            if twos == []:
                if len(ones) < 2:
                    return sum(zeros)
                else:
                    return best - ones[0] - ones[1]
            other_cand = 0
            if len(ones) >= 2:
                other_cand = best - ones[0] - ones[1]
            return max(best - twos[0], other_cand)
