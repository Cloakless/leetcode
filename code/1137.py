class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0,1,1]
        for i in range(3,38):
            tri.append(tri[i-1] + tri[i-2] + tri[i-3])
        return tri[n]
