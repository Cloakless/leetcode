class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dists = [[[0,0] for x in range(n)] for y in range(m)]
        # Calculate range to right
        for i in range(m):
            width = 0
            for j in range(n):
                if matrix[i][n-j-1] == "0":
                    width = 0
                    dists[i][n-j-1][0] = 0
                else:
                    width += 1
                    dists[i][n-j-1][0] = width
        # Calculate range below
        for a in range(n):
            depth = 0
            for b in range(m):
                if matrix[m-b-1][a] == "0":
                    depth = 0
                    dists[m-b-1][a][1] = 0
                else:
                    depth += 1
                    dists[m-b-1][a][1] = depth

        def calc_area(p,q):
            if matrix[p][q] == "0":
                return 0
            width = dists[p][q][0]
            depth = dists[p][q][1]

            curr_w = width
            area = curr_w
            for d in range(depth):
                curr_w = min(curr_w, dists[p+d][q][0])
                area = max(area, (d+1)*curr_w)
            return area

        best_area = 0
        for p in range(m):
            for q in range(n):
                best_area = max(best_area, calc_area(p,q))
        return best_area
        
