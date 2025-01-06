class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0 for _ in range(n)]
        for ball in range(n):
            if boxes[ball] == '1':
                for j in range(n):
                    ans[j] += abs(ball-j)
        return ans
