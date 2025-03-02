class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        vals = defaultdict(int)
        for idi, vali in nums1:
            vals[idi] += vali
        for idi, vali in nums2:
            vals[idi] += vali

        ans = []
        for val in vals:
            ans.append([val, vals[val]])
        return sorted(ans)

