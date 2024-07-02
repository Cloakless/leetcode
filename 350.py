class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tot = []
        nums1.sort()
        nums2.sort()
        for elem in nums1:
            if elem in nums2:
                tot.append(elem)
                nums2.remove(elem)
        return tot
