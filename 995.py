class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        num_flips = 0
        buffer_flips = 0
        flip_starts = deque()
        for index, value in enumerate(nums):
            while flip_starts and flip_starts[0] < index - k + 1:
                flip_starts.popleft()
                buffer_flips -= 1
            if (value + buffer_flips) % 2 == 0:
                if index > n - k:
                    return -1
                num_flips += 1
                buffer_flips += 1
                flip_starts.append(index)
        return num_flips
