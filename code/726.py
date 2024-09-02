class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def splitString(s):
            n = len(s)
            elems = []
            start, end = 0, 0
            while end < n - 1:
                end += 1
                if s[end].upper() == s[end] and not s[end].isdigit():
                    elems.append(s[start:end])
                    start = end
            elems.append(s[start:])
            return elems

        def extract_num(s, i):
            tot = 0
            num_digits = 0
            while True:
                try:
                    temp = s[i]
                    if temp.isdigit():
                        tot *= 10
                        tot += int(temp)
                        num_digits += 1
                    else:
                        break
                except IndexError:
                    break
                i += 1
            if tot == 0:
                return 1, 0
            return tot, num_digits

        def mult(d, n):
            # Multiply a dictionary
            for key in d:
                d[key] = d[key] * n

        def dadd(a, b):
            for key in b:
                if key not in a:
                    a[key] = b[key]
                else:
                    a[key] += b[key]
            return a

        def countString(s):
            # Count a formula without any brackets
            counter = {}
            if len(s) == 0:
                return counter
            elems = splitString(s)
            for elem in elems:
                if not elem[-1].isdigit():
                    # Only one of them
                    if elem in counter:
                        counter[elem] += 1
                    else:
                        counter[elem] = 1 
                elif elem[1].isdigit():
                    # Single letter
                    if elem[0] in counter:
                        counter[elem[0]] += int(elem[1:])
                    else:
                        counter[elem[0]] = int(elem[1:])
                else:
                    if elem[:2] in counter:
                        counter[elem[:2]] += int(elem[2:])
                    else:
                        counter[elem[:2]] = int(elem[2:])
            return counter


        def countFormula(s):
            # Count a formula with brackets
            counter = {}
            n = len(s)
            if n == 0:
                return {}
            if s == "()":
                return {}

            depth = 0
            bases = []
            for i in range(n):
                if s[i] == "(":
                    if depth == 0:
                        bases.append(i)
                    depth += 1
                if s[i] == ")":
                    depth -= 1
                    if depth == 0:
                        bases.append(i)
            if not bases:
                # Count without brackets
                counter = countString(s)
                return counter
            counter = countString(s[:bases[0]])
            while bases:
                start = bases.pop(0)
                end = bases.pop(0)
                multiplier, digits = extract_num(s, end+1)

                base_count = countFormula(s[start+1:end])
                mult(base_count, multiplier)
                counter = dadd(counter, base_count)
                if end + digits < n - 1:
                    if bases:
                        new_star = bases[0]
                    else:
                        new_star = n
                    next_form = countString(s[end + digits +1:new_star])
                    counter = dadd(counter, next_form)
            return counter
        results = countFormula(formula)
        counts = []
        for key in results:
            counts.append((key, results[key]))
        counts.sort()
        ans_string = ""
        for count in counts:
            ans_string += count[0]
            if count[1] != 1:
                ans_string += str(count[1])
        return ans_string
