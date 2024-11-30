class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        if len(pairs) == 1:
            return pairs
        neighbours = defaultdict(set)
        ins = defaultdict(int)
        outs = defaultdict(int)
        nodes = set()
        path_start, path_end = None, None
        for start, end in pairs:
            neighbours[start].add(end)
            outs[start] += 1
            ins[end] += 1
            nodes.add(start)
            nodes.add(end)
        for node in nodes:
            if ins[node] < outs[node]:
                path_start = node
            elif ins[node] > outs[node]:
                path_end = node
        if path_start is None:
            path_start = nodes.pop()
            nodes.add(path_start)
            path_end = path_start
        curr_node = path_start
        curr_node = neighbours[path_start].pop()
        path = [path_start, curr_node]
        while curr_node != path_end:
            curr_node = neighbours[curr_node].pop()
            path.append(curr_node)
        adding = True
        while adding:
            ans = []
            adding = False
            for node in path:
                ans.append(node)
                while neighbours[node]:
                    adding = True
                    curr_node = neighbours[node].pop()
                    ans.append(curr_node)
                    while curr_node != node:
                        curr_node = neighbours[curr_node].pop()
                        ans.append(curr_node)
                path = ans
        ans_list = []
        for i in range(len(ans)-1):
            ans_list.append([ans[i], ans[i+1]])
        return ans_list
           
        
