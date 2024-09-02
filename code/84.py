class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        w = len(heights)
        h = max(heights)
        nearest = [[-2, -2] for n in range(w)]

        nearest[0][0] = -1
        nearest[w-1][1] = w

        # Flatten where possible
        changing = True
        while changing:
            changing = False
            for m in range(1, w-1):
                if heights[m-1] < heights[m] and heights[m+1] < heights[m]:
                    heights[m] = max(heights[m-1], heights[m+1])
                    changing = True

        for i in range(1,w):
            if heights[i-1] < heights[i]:
                nearest[i][0] = i-1
        for i in range(w-1):
            if heights[i+1] < heights[i]:
                nearest[i][1] = i+1

        # Check monotonic from start and end
        for i in range(1, w):
            if heights[i-1] >= heights[i]:
                nearest[i][0] = -1
            else:
                nearest[i][0] = i-1
                break
        for i in range(w-1)[::-1]:
            if heights[i] <= heights[i+1]:
                nearest[i][1] = w
            else:
                nearest[i][1] = i+1
                break

        for i in range(1,w):
            if heights[i-1] == heights[i]:
                nearest[i][0] = nearest[i-1][0]
        for i in range(w-1)[::-1]:
            if heights[i+1] == heights[i]:
                nearest[i][1] = nearest[i+1][1]

        def calc_area(p):
            h = heights[p]
            if h == 0:
                return 0
            L = p
            R = p
            if nearest[p][0] != -2:
                nearest_l = nearest[p][0]
            else:
                while L >= 0:
                    if heights[L] < h:
                        nearest_l = L
                        break
                    else:
                        L -= 1
                        if L == -1:
                            nearest_l = -1
            if nearest[p][1] != -2:
                nearest_r = nearest[p][1]
            else:
                while R <= w-1:
                    if heights[R] < h:
                        nearest_r = R
                        break
                    else:
                        R += 1
                        if R == w:
                            nearest_r = w
            return h * (nearest_r - nearest_l - 1)

        best_area = h
        for cell in range(w):
            best_area = max(best_area, calc_area(cell))
            if best_area >= h * w:
                break

        return best_area
