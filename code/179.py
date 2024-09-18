class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        ans = sorted(strs, key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return "".join(ans) if set(ans) != {"0"} else "0"
