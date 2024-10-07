class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: -1*(x[0] - x[1]/10000000))
        ans = []
        for i in range(n):
            height, forwards = people[i]
            ans = ans[:forwards] + [[height, forwards]] + ans[forwards:]
        return ans
