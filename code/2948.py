class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        s_list = sorted(nums)
        n = len(nums)
        group = {}
        group_elems = defaultdict(deque)
        group_num = 0
        group_elems[group_num].append(s_list[0])
        group[s_list[0]] = group_num

        # Determine what order each number is in within its group
        for i in range(1, n):
            if s_list[i] - s_list[i-1] > limit:
                group_num += 1
            group[s_list[i]] = group_num
            group_elems[group_num].append(s_list[i])

        for j in range(n):
            opt = group[nums[j]]
            nums[j] = group_elems[opt].popleft()
        return nums
