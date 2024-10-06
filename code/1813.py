class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split()
        l2 = sentence2.split()

        def subset(a, b):
            m = len(a)
            n = len(b)
            if m > n:
                a, b = b, a
                m, n = n, m
            divergence = m
            for i in range(m):
                if a[i] != b[i]:
                    divergence = i
                    break
            if divergence == m:
                return True
            for j in range(divergence, m):
                if a[j] != b[n-m+j]:
                    return False
            return True
        return subset(l1, l2)
