class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        all_nums = []
        for i, lst in enumerate(nums):
            for num in lst:
                heappush(all_nums, (num, i))
        cand, origin = heappop(all_nums)
        scratch = [(cand, origin)]
        best = 10000000
        best_i, best_j = -1000000, 1000000
        i, j = 0, 0
        num_distinct = 1
        counter = [0]*k
        counter[scratch[0][1]] += 1

        while num_distinct < k:
            cand, origin  = heappop(all_nums)
            if counter[origin] == 0:
                num_distinct += 1
            counter[origin] += 1
            scratch.append((cand, origin))
            j += 1
        while counter[scratch[i][1]] > 1:
            # We can remove the ith one
            counter[scratch[i][1]] -= 1
            i += 1
        if scratch[j][0] - scratch[i][0] < best:
            best = min(best, scratch[j][0] - scratch[i][0])
            best_j, best_i = scratch[j][0], scratch[i][0]
        while all_nums:
            cand, origin = heappop(all_nums)
            counter[origin] += 1
            scratch.append((cand, origin))
            j += 1
            while counter[scratch[i][1]] > 1:
                # We can remove the ith one
                counter[scratch[i][1]] -= 1
                i += 1
            if scratch[j][0] - scratch[i][0] < best:
                best = min(best, scratch[j][0] - scratch[i][0])
                best_j, best_i = scratch[j][0], scratch[i][0]
        return [best_i, best_j]
