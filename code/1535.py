class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        arr = deque(arr)
        streak = 0
        while True:
            a = arr.popleft()
            b = arr.popleft()
            if streak == k:
                return a
            if b > a:
                streak = 1
                arr.appendleft(b)
                arr.append(a)
            else:
                streak += 1
                arr.appendleft(a)
                arr.append(b)
