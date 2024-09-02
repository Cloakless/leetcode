class Solution:
    def checkValidString(self, s: str) -> bool:
        doing_things = True
        while doing_things:
            doing_things = False
            n = len(s)
            if n == 0:
                return True
            elif n == 1:
                if s[0] == '*':
                    return True
                else:
                    return False
            removing = True
            while removing:
                removing = False
                i = 0
                temp = []
                n = len(s)
                while i < n:
                    try:
                        if s[i] == "(" and s[i+1] == ")":
                            i += 2
                            removing = True
                            doing_things = True
                        else:
                            temp.append(s[i])
                            i += 1
                    except IndexError:
                        temp.append(s[i])
                        i += 1
                s = "".join(temp)
            new = s
            m = len(new)
            if m == 0:
                return True
            elif m == 1:
                if new[0] == '*':
                    return True
                else:
                    return False
            
            shrinking = True
            while shrinking:
                shrinking = False
                if new[0] == "(" and new[-1] == ")":
                    new = new[1:-1]
                    shrinking = True
                    doing_things = True
                elif new[-1] == "(":
                    return False
                m = len(new)
                if m == 0:
                    return True
                elif m == 1:
                    if new[0] == '*':
                        return True
                    else:
                        return False
            doing_things = False


        counter = 0
        stars = 0
        r_stars = 0
        for char in s:
            if char == "(":
                counter += 1
            elif char == "*":
                stars += 1
                r_stars += 1

            else:
                if counter == 0:
                    if stars > 0:
                        stars -= 1
                        r_stars -= 1
                    else:
                        return False
                else:
                    counter -= 1
            if r_stars > counter:
                r_stars = counter
        if counter > 0 and counter > r_stars:
            return False
        return True
