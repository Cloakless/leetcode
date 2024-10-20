class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse_letter(s):
            return s == 't'

        def parse(string):
            print("parsing {}".format(string))
            n = len(string)
            if n == 1:
                return parse_letter(string)
            if string[0] == '!':
                return invert(string[2:n-1])
            elif string[0] == '&':
                return parse_and(string[2:n-1])
            elif string[0] == '|':
                return parse_or(string[2:n-1])
            else:
                assert False, "Faulty string {}".format(string)

            
        def invert(string):
            return not parse(string)

        def lst_split(string):
            str_lst = list(string)
            height = 0
            for i, elem in enumerate(str_lst):
                if elem == '(':
                    height += 1
                elif elem == ')':
                    height -= 1
                elif elem == ',' and height == 0:
                    str_lst[i] = '*'
            lst = "".join(str_lst).split('*')
            return lst
        
        def parse_and(string):
            lst = lst_split(string)
            acc = True
            for subex in lst:
                acc = acc and parse(subex)
            return acc

        def parse_or(string):
            lst = lst_split(string)
            acc = False
            for subex in lst:
                acc = acc or parse(subex)
            return acc

        return parse(expression)
