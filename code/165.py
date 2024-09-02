class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")
        if len(a) > len(b):
            for j in range((len(a)-len(b))):
                b.append('0')
        elif len(b) > len(a):
            for j in range(len(b)-len(a)):
                a.append('0')
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                return 1
            elif int(b[i]) > int(a[i]):
                return -1
        return 0
