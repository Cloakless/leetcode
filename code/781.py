class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = defaultdict(int)
        for answer in answers:
            counter[answer+1] += 1
        ans = 0
        for opt in counter:
            num = counter[opt]
            ans += math.ceil(num/opt)*opt
        return ans
