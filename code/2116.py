class Solution:
    def canBeValid(self, s, locked):
        if len(s) % 2 == 1:
            return False
        unused = 0
        height = 0
        locks = set()
        for i in range(len(locked)):
            if locked[i] == '1':
                locks.add(i)
        for i in range(len(s)):
            if i in locks:
                if s[i] == '(':
                    height += 1
                else:
                    height -= 1
                if height == -1:
                    if unused == 0:
                        return False
                    else:
                        height += 1
                        unused -= 1
            else:
                unused += 1

        excess = 0
        for i in reversed(range(len(s))):
            if locked[i] == '0':
                excess -= 1
                unused -= 1
            else:
                if s[i] == '(':
                    excess += 1
                    height -= 1
                if s[i] == ')':
                    excess -= 1
            if excess > 0:
                return False
            if unused == 0 and height == 0:
                break
        return height <= 0
