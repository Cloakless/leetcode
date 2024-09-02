class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Add an end marker
        expression += '!'
        if expression[0] == '-':
            operation = -1
        else:
            operation = 1
            expression = '+' + expression
        n = len(expression)
        pointer = 0
        num = 0
        denom = 1
        primes = [2,3,5,7]
        while pointer < n:
            # Get next operation
            if expression[pointer] == '+':
                operation = 1
            elif expression[pointer] == '-':
                operation = -1
            elif expression[pointer] == '!':
                return "{}/{}".format(num,denom)
            pointer += 1
            # Get numerator
            tot = 0
            while expression[pointer].isnumeric():
                tot *= 10
                tot += int(expression[pointer])
                pointer += 1
            newnum = tot
            # Skip /
            pointer += 1
            # Get denominator
            tot = 0
            while expression[pointer].isnumeric():
                tot *= 10
                tot += int(expression[pointer])
                pointer += 1
            newdenom = tot
            # Add to current total
            num, denom, newnum, newdenom = num*newdenom, denom*newdenom, newnum*denom, newdenom*denom
            num = num + operation*newnum
            # Simplify
            for prime in primes:
                while num % prime == 0 and denom % prime == 0:
                    num //= prime
                    denom //= prime
