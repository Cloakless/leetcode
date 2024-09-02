class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        rights = [] 
        n = len(positions)    
        finals = [0 for _ in range(n)]  
        robots = list(zip(positions, healths, directions, range(n)))
        robots.sort()
        for robot in robots:
            if robot[2] == 'R':
                rights.append(list(robot))
            else:
                robot = list(robot)
                # Robot is going left; equivalent to stationary since we do not care about final position
                while robot[1] > 0 and rights:
                    r_health, l_health = rights[-1][1], robot[1]
                    if l_health < r_health:
                        # Left is weaker, destroyed
                        finals[robot[3]] = 0
                        rights[-1][1] -= 1
                        robot[1] = 0
                    elif l_health > r_health:
                        # Right is weaker, destroyed
                        right = rights.pop()
                        finals[right[3]] = 0
                        robot[1] -= 1
                    else:
                        # Both are destroyed
                        right = rights.pop()
                        finals[right[3]] = 0
                        finals[robot[3]] = 0
                        robot[1] = 0
                if robot[1] > 0:
                    # No more collisions
                    finals[robot[3]] = robot[1]
        while rights:
            right = rights.pop()
            finals[right[3]] = right[1]
        return [i for i in finals if i > 0]
