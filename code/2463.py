class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robots = sorted(robot)
        factories = []
        for position, mult in factory:
            for i in range(mult):
                factories.append(position)
        factories.sort()
        num_robots = len(robots)
        num_factories = len(factories)

        @lru_cache(maxsize=10000)
        def min_dist(robot_i, factory_i):
            if robot_i >= num_robots:
                return 0
            if (num_robots - robot_i) > (num_factories - factory_i):
                return 1000000000000000
            select_first = abs(robots[robot_i] - factories[factory_i]) + min_dist(robot_i + 1, factory_i + 1)
            select_next = min_dist(robot_i, factory_i + 1)
            return min(select_first, select_next)
        
        return min_dist(0,0)
        
