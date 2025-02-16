class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0]*(2*n - 1)
        used = [False for _ in range(n)]
        def search(pointer):
            if all(used):
                return True
            if pointer >= 2*n - 1:
                return False
            if ans[pointer] > 0:
                return search(pointer+1)

            for num in reversed(range(n)):
                if used[num] == True:
                    continue
                if num == 0:
                    used[num] = True
                    ans[pointer] = 1
                    if search(pointer + 1):
                        return True
                    used[num] = False
                    ans[pointer] = 0
                    return False

                if pointer + num + 1 >= 2*n - 1:
                    return False
                if ans[pointer+num+1] == 0:

                    ans[pointer] = num + 1  
                    ans[pointer+num+1] = num + 1
                    used[num] = True
                    if search(pointer+1):
                        return True
                    used[num] = False
                    ans[pointer+num+1] = 0
            ans[pointer] = 0
            return False

        search(0)
        return ans
