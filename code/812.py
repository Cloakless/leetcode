class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def heron(x1, y1, x2, y2, x3, y3):
            a = ((x2-x1)**2 + (y2-y1)**2)**0.5
            b = ((x3-x1)**2 + (y3-y1)**2)**0.5
            c = ((x3-x2)**2 + (y3-y2)**2)**0.5
            s = 0.5*(a+b+c)
            if s < a or s < b or s < c:
                return 0
            return (s*(s-a)*(s-b)*(s-c))**0.5

        best = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    best = max(best, heron(x1,y1,x2,y2,x3,y3))
        return best
    
