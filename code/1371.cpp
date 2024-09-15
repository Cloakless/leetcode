class Solution {
public:
    int findTheLongestSubstring(string s) {
        unordered_map<char, int> vowels = {{'a', 1}, {'e', 2}, {'i', 4}, {'o', 8}, {'u', 16}};
        vector<int> bitmask(s.size(), 0);
        if (vowels.contains(s[0])) {
            bitmask[0] = vowels[s[0]];
        }
        else {
            bitmask[0] = 0;
        }
        for (int i = 1; i < s.size(); i++) {
            if (vowels.contains(s[i])) {
                bitmask[i] = bitmask[i-1]^vowels[s[i]];
            }
            else {
                bitmask[i] = bitmask[i-1];
            }
        }
        int best = 0;
        unordered_map<int, int> earliest;
        earliest[0] = -1; // So we can have the entire string
        
        for (int j = 0; j < s.size(); j++) {
            if (earliest.contains(bitmask[j])) {
                best = max(j-earliest[bitmask[j]], best);
            }
            else {
                earliest[bitmask[j]] = j;
            }
        }
        return best;
    }
};
