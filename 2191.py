class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def intmap(num):
            num = list(str(num))
            for i in range(len(num)):
                num[i] = str(mapping[int(num[i])])
            num = int("".join(num))
            return num
        nums.sort(key=lambda x: intmap(x))
        return nums
