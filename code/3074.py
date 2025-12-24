class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort()
        capacity = capacity[::-1]
        ans = 0
        while apples > 0:
            ans += 1
            apples -= capacity[ans-1]
        return ans
