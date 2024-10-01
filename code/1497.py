class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = list(map(lambda x: x % k, arr))
        arr.sort()
        n = len(arr)
        first = 0
        last = n - 1
        num_zeros = 0
        while first < n and arr[first] == 0:
            first += 1
            num_zeros += 1
        if num_zeros % 2 != 0:
            return False
        while first < last:
            if arr[first] + arr[last] != k:
                return False
            first += 1
            last -= 1
        return True
