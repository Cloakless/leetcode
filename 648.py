class Solution:
    class TrieNode:
        def __init__(self):
            self.children = collections.defaultdict(Solution.TrieNode)
            self.is_end = False

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert(self, word):
            current = self.root
            for letter in word:
                current = current.children[letter]
            current.is_end = True

        def search(self, word):
            current = self.root
            for letter in word:
                current = current.children.get(letter)
                if current is None:
                    return False
            return current.is_end

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Solution.Trie()
        for word in dictionary:
            trie.insert(word)

        def redact(word):
            for i in range(len(word)):
                prefix = word[:i+1]
                if trie.search(prefix):
                    return prefix
            return word

        for j in range(len(words)):
            words[j] = redact(words[j])

        return " ".join(words)
