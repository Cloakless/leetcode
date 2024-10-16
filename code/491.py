class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def get_subs(lst):
            if len(lst) == 0:
                return []
            ans = [[lst[0]]]
            subs = get_subs(lst[1:])
            for sub in subs:
                ans.append(sub)
                if sub[0] >= lst[0]:
                    ans.append([lst[0]] + sub)
            return ans
        cands = set(map(tuple, get_subs(nums)))

        return [list(cand) for cand in cands if len(cand) > 1]
