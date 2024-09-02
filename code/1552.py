class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def isPossible(d):
            num_balls = m - 1
            last_ball = position[0]
            for i in range(1, n):
                if position[i] - last_ball >= d:
                    num_balls -= 1
                    last_ball = position[i]
                    if num_balls == 0:
                        return True
            return False

        left = 1
        right = position[-1] - position[0] + 1
        while left < right - 1:
            test = int((left + right)/2)
            test_result = isPossible(test)
            if test_result:
                left = test
            else:
                right = test

        return right - 1
