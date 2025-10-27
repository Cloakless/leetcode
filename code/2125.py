class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])
        devices = [row.count("1") for row in bank]
        temp = []
        for num in devices:
            if num > 0:
                temp.append(num)
        devices = temp
        ans = 0
        if len(devices) <= 1:
            return 0
        for i in range(len(devices)-1):
            ans += devices[i]*devices[i+1]
        return ans
