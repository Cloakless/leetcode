class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        files = set()
        for file in folder:
            path = tuple(file[1:].split('/'))
            files.add(path)
        ans = []
        for file in files:
            valid = True
            for i in range(len(file)):
                if file[:i] in files:
                    valid = False
                    break
            if valid:
                ans.append("/" + "/".join(file))
        return ans
        
