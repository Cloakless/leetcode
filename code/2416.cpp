struct TrieNode {
    unordered_map<char, TrieNode*> next;
    int count = 0;
};

class Solution {
    TrieNode root;
public:
    void insert(string word) {
        TrieNode* node = &root;
        for (char c: word) {
            if (!node->next.contains(c)) {
                node->next[c] = new TrieNode();
            }
            node->next[c]->count++;
            node = node->next[c];
        }
    }
    int count(string word) {
        int ans = 0;
        TrieNode* node = &root;
        for (char c: word) {
            ans += node->next[c]->count;
            node = node->next[c];
        }
        return ans;
    }
    vector<int> sumPrefixScores(vector<string>& words) {
        int n = words.size();
        for (string word: words) {
            insert(word);
        }
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            ans[i] = count(words[i]);
        }
        return ans;
    }
};
