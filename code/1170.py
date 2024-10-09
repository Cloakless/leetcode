class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            n = len(s)
            if n == 1:
                return 1
            sl = list(s)
            sl.sort()
            num = 1
            for pointer in range(1, n):
                if sl[pointer] == sl[0]:
                    num += 1
                else:
                    return num
            return num
        for i in range(len(words)):
            words[i] = f(words[i])
        words.sort()
        m = len(words)

        def num_bigger(a):
            if a < words[0]:
                return m
            if a >= words[m-1]:
                return 0
            lower = 0
            upper = m-1
            while lower + 1 < upper:
                mid = (lower + upper)//2
                if words[mid] > a:
                    upper = mid
                else:
                    lower = mid
            if words[lower] > a:
                return m - lower
            else:
                return m - lower -1
        return [num_bigger(f(query)) for query in queries]
