class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        if right == 0:
            return 1
        tot = 0
        while left <= right:
            tot += 1
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
        return tot
