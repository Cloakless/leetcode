class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def max_points(i):
            if i >= n:
                return 0
            return max(max_points(i+1), questions[i][0] + max_points(i+questions[i][1]+1))
        return max_points(0)
