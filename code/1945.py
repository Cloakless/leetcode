class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = "".join(list(map(lambda x: str(ord(x) - 96), list(s))))
        for _ in range(k):
            n = sum(list(map(lambda x: int(x), list(str(n)))))
        return n
