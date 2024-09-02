class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(map(lambda x: int(int(x[11:13]) > 60), details))
