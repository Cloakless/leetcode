class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        balls = defaultdict(int)
        num_balls = defaultdict(int)
        colours = 0
        for ball, colour in queries:
            if balls[ball] == 0:
                # New colour
                balls[ball] = colour
                num_balls[colour] += 1
                if num_balls[colour] == 1:
                    colours += 1
            else:
                prev_colour = balls[ball]
                num_balls[prev_colour] -= 1
                if num_balls[prev_colour] == 0:
                    colours -= 1
                balls[ball] = colour
                num_balls[colour] += 1
                if num_balls[colour] == 1:
                    colours += 1
            ans.append(colours)
        return ans
