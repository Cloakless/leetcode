class Solution:
    def get_subs(lst):
        ans = [[lst[0]]]
        if len(lst) == 1:
            return ans
        cands = Solution.get_subs(lst[1:])
        for cand in cands:
            ans.append(cand)
            ans.append([lst[0]] + cand)
        return ans

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        tot, target = 0, 0
        n = len(nums)
        for num in nums:
            target |= num

        for opt in Solution.get_subs(nums):
            counter = 0
            for num in opt:
                counter |= num
                if counter == target:
                    tot += 1
                    break

        return tot
        
