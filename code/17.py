class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lets = {1: [''], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']}
        ans = []
        def process(start, rem):
            if len(rem) == 0:
                if len(start) > 0:
                    ans.append(start)
            else:
                for let in lets[int(rem[0])]:
                    process(start + let, rem[1:])
        process('', digits)
        return ans
