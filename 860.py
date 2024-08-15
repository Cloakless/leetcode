class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0,0,0]
        notes = {5: 0, 10: 1, 20: 2}
        for bill in bills:
            cash[notes[bill]] += 1
            if bill == 20:
                if cash[1] > 0 and cash[0] > 0:
                    cash[1] -= 1
                    cash[0] -= 1
                elif cash[0] > 2:
                    cash[0] -= 3
                else:
                    return False
            elif bill == 10:
                if cash[0] > 0:
                    cash[0] -= 1
                else:
                    return False
        return True
