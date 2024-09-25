class TrieNode {
public:
    TrieNode* children[26];
    bool is_word;
    TrieNode() {
        is_word = false;
        for (TrieNode* &c: children) {
            c = NULL;
        }
        for (TrieNode* c: children) {
        }
    }
};

class Trie {
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* curr = root;
        for (char c: word) {

            TrieNode* &target = curr->children[c-'a'];
            if (target == NULL) {
                target = new TrieNode();
            }
            curr = target;
        }
        curr->is_word = true;
        
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            TrieNode* target = curr->children[c-'a'];
            if (target == NULL) {
                return false;
            }
            curr = target;
        }     
        if (curr->is_word) {
            return true;
        }
        return false;
    }
    
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for (char c : prefix) {
            TrieNode* target = curr->children[c-'a'];
            if (target == NULL) {
                return false;
            }
            curr = target;
        }     
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
