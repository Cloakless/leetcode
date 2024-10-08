class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counter = defaultdict(int)
        subs = 0
        for char in s:
            if char == '?':
                subs += 1
            else:
                counter[ord(char)-97] += 1
        letter_heap = []
        new_lets = []
        heapq.heapify(letter_heap)
        for i in range(26):
            if counter[i] != 0:
                heapq.heappush(letter_heap, (counter[i], i))
            else:
                heapq.heappush(letter_heap, (0, i))
        for j in range(subs):
            freq, letter = heapq.heappop(letter_heap)
            new_lets.append(chr(letter+97))
            heapq.heappush(letter_heap, (freq+1, letter))
        new_lets.sort()
        s_lst = list(s)
        idx = 0
        for i, letter in enumerate(s_lst):
            if letter == '?':
                s_lst[i] = new_lets[idx]
                idx += 1
        return "".join(s_lst)
